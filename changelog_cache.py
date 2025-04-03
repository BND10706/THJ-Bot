import os
import json
import logging
import asyncio
import time
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional, Any, Callable, Awaitable
import aiofiles # Using aiofiles for async file operations
import traceback # <--- Add this import

# Use logger from config to ensure consistent logging format
from config import logger

# Define how many entries to look back during incremental refreshes
INCREMENTAL_REFRESH_LOOKBACK = 5

# Cache file path
CACHE_FILE = 'changelog_cache.json'
# Refresh interval (e.g., every 15 minutes)
REFRESH_INTERVAL_SECONDS = 60 # Changed from 15 * 60
# Stale threshold (e.g., if cache is older than 30 minutes, force refresh on read)
STALE_THRESHOLD_SECONDS = 30 * 60

class ChangelogCacheManager:
    def __init__(self):
        self._cache = {"changelogs": [], "last_updated": None, "version": 2} # Versioning cache format
        self._lock = asyncio.Lock() # Lock for async operations on cache/file
        self._get_changelog_func: Optional[Callable[..., Awaitable[Dict[str, Any]]]] = None
        self._periodic_refresh_task: Optional[asyncio.Task] = None
        self._is_initialized = False
        logger.info("ChangelogCacheManager initialized.")

    def register_get_changelog_func(self, func: Callable[..., Awaitable[Dict[str, Any]]]):
        """Registers the async function used to fetch changelogs."""
        self._get_changelog_func = func
        logger.info(f"Registered changelog fetch function: {func.__name__}")

    async def _load_cache_from_file(self):
        """Load cache data from the JSON file."""
        async with self._lock: # Ensure exclusive access during load
            if not os.path.exists(CACHE_FILE):
                logger.warning(f"Cache file '{CACHE_FILE}' not found. Starting with empty cache.")
                self._cache = {"changelogs": [], "last_updated": None, "version": 2}
                return

            try:
                async with aiofiles.open(CACHE_FILE, mode='r', encoding='utf-8') as f:
                    content = await f.read()
                    if not content: # Handle empty file
                         logger.warning(f"Cache file '{CACHE_FILE}' is empty. Starting with empty cache.")
                         self._cache = {"changelogs": [], "last_updated": None, "version": 2}
                         return

                    data = json.loads(content)
                    # Basic validation and migration if needed
                    if isinstance(data, dict) and "changelogs" in data and "last_updated" in data:
                         # Version check (optional, for future format changes)
                         if data.get("version") == 2:
                            self._cache = data
                            # Ensure changelogs is a list
                            if not isinstance(self._cache.get("changelogs"), list):
                                logger.error("Loaded cache has invalid 'changelogs' format. Resetting.")
                                self._cache["changelogs"] = []
                            # Parse timestamp
                            if self._cache["last_updated"]:
                                try:
                                    # Ensure timestamp is timezone-aware (UTC)
                                    ts = datetime.fromisoformat(self._cache["last_updated"])
                                    if ts.tzinfo is None:
                                        self._cache["last_updated"] = ts.replace(tzinfo=timezone.utc).isoformat()
                                    else:
                                         self._cache["last_updated"] = ts.astimezone(timezone.utc).isoformat()
                                except (ValueError, TypeError):
                                    logger.error("Failed to parse last_updated timestamp from cache file. Resetting.")
                                    self._cache["last_updated"] = None

                            logger.info(f"Successfully loaded cache from '{CACHE_FILE}'. "
                                        f"Entries: {len(self._cache.get('changelogs', []))}. "
                                        f"Last updated: {self._cache.get('last_updated', 'Never')}")
                         else:
                              logger.warning(f"Cache file version mismatch (found {data.get('version')}, expected 2). Discarding old cache.")
                              self._cache = {"changelogs": [], "last_updated": None, "version": 2}
                    else:
                        logger.error(f"Invalid cache file format in '{CACHE_FILE}'. Discarding content.")
                        self._cache = {"changelogs": [], "last_updated": None, "version": 2}

            except json.JSONDecodeError:
                logger.error(f"Failed to decode JSON from cache file '{CACHE_FILE}'. Starting fresh.")
                self._cache = {"changelogs": [], "last_updated": None, "version": 2}
            except Exception as e:
                logger.error(f"Error loading cache file '{CACHE_FILE}': {e}")
                self._cache = {"changelogs": [], "last_updated": None, "version": 2}

    async def _save_cache_to_file_internal(self):
        """Saves the current cache to file. ASSUMES LOCK IS HELD."""
        # Log *immediately* upon entry
        logger.debug(f"--- Executing internal save ---")
        try:
            # Ensure last_updated is set correctly before saving
            if not self._cache.get("last_updated"):
                 self._cache["last_updated"] = datetime.now(timezone.utc).isoformat()
                 logger.debug(f"Set last_updated timestamp (internal save).")

            abs_cache_file_path = os.path.abspath(CACHE_FILE)
            logger.debug(f"Target cache file path (internal save): {abs_cache_file_path}")

            logger.debug(f"--> Preparing JSON data (internal save)...")
            json_data = json.dumps(self._cache, indent=2)
            logger.debug(f"--> JSON data prepared (length: {len(json_data)}) (internal save).")

            logger.debug(f"--> About to open '{abs_cache_file_path}' for writing (internal save)...")
            async with aiofiles.open(CACHE_FILE, mode='w', encoding='utf-8') as f:
                logger.debug(f"File '{abs_cache_file_path}' opened successfully (internal save).")
                await f.write(json_data)
                logger.debug(f"Finished writing to '{abs_cache_file_path}' (internal save).")

            logger.debug(f"✅ Cache successfully saved via internal method to '{abs_cache_file_path}'.")
        except Exception as e:
            abs_cache_file_path = os.path.abspath(CACHE_FILE)
            logger.error(f"❌ Error during internal save to file '{abs_cache_file_path}': {e}")
            logger.debug(traceback.format_exc())

    async def save_cache_to_file_public_safe(self):
        """Public method to save cache, acquiring the lock."""
        logger.info("--- Public save request: Attempting lock ---")
        async with self._lock:
            logger.debug("--- Public save request: Lock acquired ---")
            await self._save_cache_to_file_internal()
            logger.debug("--- Public save request: Lock released ---")

    async def initialize(self):
        """Loads cache from file and performs initial refresh if needed."""
        if self._is_initialized:
            return
        logger.info("Initializing Changelog Cache Manager...")
        await self._load_cache_from_file()
        # Perform an initial refresh on startup to ensure cache isn't stale
        # Use a longer stale threshold for the initial load check
        initial_stale_threshold = timedelta(hours=1) # e.g., refresh if older than 1 hour
        needs_initial_refresh = True # Default to refresh
        if self._cache["last_updated"]:
            try:
                last_update_time = datetime.fromisoformat(self._cache["last_updated"])
                if datetime.now(timezone.utc) - last_update_time < initial_stale_threshold:
                    needs_initial_refresh = False
                    logger.info("Cache is recent enough, skipping initial full refresh.")
            except ValueError:
                 logger.error("Invalid timestamp in cache during initialization, forcing refresh.")

        if needs_initial_refresh:
             logger.info("Performing initial cache refresh...")
             await self.refresh(force=True) # Force a full refresh initially
        else:
             logger.info("Performing initial incremental cache check...")
             await self.refresh(force=False) # Perform incremental check

        self._is_initialized = True
        logger.info("Changelog Cache Manager initialized successfully.")
        
    async def refresh(self, force: bool = False) -> Optional[int]:
        """
        Refreshes the cache by fetching new changelogs.
        Acquires lock for the duration of cache modification and saving.
        """
        if not self._get_changelog_func:
            logger.error("Cannot refresh cache: get_changelog function not registered.")
            return None
            
        # Lock is acquired here for the whole refresh process involving cache modification
        async with self._lock:
            logger.info(f"Starting cache refresh (force={force}) - Lock acquired.")
            try:
                latest_cached_id = None
                # Determine latest_cached_id (safe under lock)
                if not force and self._cache["changelogs"]:
                    # Sort just in case, find the actual latest ID
                    self._cache["changelogs"].sort(key=lambda x: int(x["id"]), reverse=True)
                    latest_cached_id = self._cache["changelogs"][0]["id"]
                    logger.debug(f"Incremental refresh: fetching messages after ID {latest_cached_id}")
                else:
                    logger.debug("Full refresh: forcing or cache empty.")

                # --- Fetching (can happen outside lock, but simpler to keep locked for now) ---
                if force:
                    fetched_data = await self._get_changelog_func(all=True, is_cache_refresh=True)
                else:
                    fetched_data = await self._get_changelog_func(message_id=latest_cached_id, limit=INCREMENTAL_REFRESH_LOOKBACK, is_cache_refresh=True)

                if fetched_data and fetched_data.get("status") == "success":
                    new_changelogs = fetched_data.get("changelogs", [])
                    if not new_changelogs and not force:
                         logger.info("Incremental refresh: No new changelogs found.")
                         self._cache["last_updated"] = datetime.now(timezone.utc).isoformat()
                         # Save the updated timestamp using the INTERNAL method
                         await self._save_cache_to_file_internal() # Already holds lock
                         return len(self._cache["changelogs"])

                    logger.info(f"Refresh fetched {len(new_changelogs)} changelogs.")

                    # --- Processing and Cache Update (under lock) ---
                    if force:
                        self._cache["changelogs"] = new_changelogs
                        logger.info(f"Full refresh processing complete. Cache now contains {len(self._cache['changelogs'])} entries in memory.")
                    else:
                        # Incremental refresh: add new entries, avoid duplicates
                        existing_ids = {entry["id"] for entry in self._cache["changelogs"]}
                        added_count = 0
                        for entry in new_changelogs:
                            if entry["id"] not in existing_ids:
                                self._cache["changelogs"].append(entry)
                                existing_ids.add(entry["id"]) # Add to set immediately
                                added_count += 1
                        logger.info(f"Incremental refresh added {added_count} new entries to memory.")

                    # Sort and update timestamp (under lock)
                    self._cache["changelogs"].sort(key=lambda x: int(x["id"]), reverse=True)
                    self._cache["last_updated"] = datetime.now(timezone.utc).isoformat()

                    # *** Save using INTERNAL method ***
                    await self._save_cache_to_file_internal() # Already holds lock
                    # No need for the separate log message here, internal save logs completion

                    # *** Deduplicate using INTERNAL method ***
                    dedup_result = await self._deduplicate_cache_internal(save_after_dedupe=True) # Already holds lock
                    if dedup_result.get("removed_count", 0) > 0:
                        logger.warning(f"Removed {dedup_result['removed_count']} duplicates during refresh (cache saved again via internal).")
                    else:
                         logger.debug("No duplicates found during post-refresh check.")

                    total_count = len(self._cache["changelogs"])
                    logger.info(f"Cache refresh finished. Final total entries: {total_count}")
                    return total_count
                else:
                    error_detail = fetched_data.get("detail", "No detail provided") if fetched_data else "Fetch function returned None"
                    logger.error(f"Failed to fetch changelogs during refresh: {error_detail}")
                    return None

            except Exception as e:
                logger.error(f"Error during cache refresh processing: {e}")
                logger.debug(traceback.format_exc())
                return None
            finally:
                 logger.info(f"Cache refresh attempt finished - Releasing lock.")

    def add_single_changelog(self, message_data: Dict[str, Any]) -> bool:
        """
        Adds a single new changelog message to the cache if it's not already present.
        Designed to be called by on_message handler (assumed async). Saves cache immediately.
        Returns True if added, False otherwise (e.g., duplicate).
        """
        if not isinstance(message_data, dict) or "id" not in message_data:
            logger.error("Invalid message_data format provided to add_single_changelog.")
            return False

        message_id = message_data["id"] # Define message_id here

        async def _add_and_save():
             async with self._lock:
                 existing_ids = {entry["id"] for entry in self._cache["changelogs"]}
                 if message_id not in existing_ids:
                     logger.debug(f"Adding single new changelog (ID: {message_id}) to cache.")
                     self._cache["changelogs"].insert(0, message_data)
                     self._cache["changelogs"].sort(key=lambda x: int(x["id"]), reverse=True)
                     self._cache["last_updated"] = datetime.now(timezone.utc).isoformat()
                     await self._save_cache_to_file_internal() # Call internal save
                     return True
                 else:
                     logger.debug(f"Changelog ID {message_id} already exists in cache. Skipping add.")
                     return False
        try:
            # Since discord.py event handlers are async, we should schedule this
            # Don't block the event handler with run_until_complete or await result directly
            # Fire and forget, or manage the task if completion status is needed elsewhere
            asyncio.create_task(_add_and_save())
            # We can't reliably return True/False immediately anymore
            # Return value indicates task creation, not addition success
            # Let's return True to indicate it was processed, log errors internally
            return True # Indicates the add process was initiated
        except Exception as e:
             # This exception is unlikely if create_task succeeds
             logger.error(f"Error creating task for adding single changelog {message_id}: {e}")
             return False # Indicates failure to even start the process
    
    async def get_cached(self, force_refresh: bool = False) -> Dict[str, Any]:
        """
        Gets the cached changelogs.
        If force_refresh is True, performs a refresh first.
        If cache is considered stale, attempts an incremental refresh.
        """
        if not self._is_initialized:
            await self.initialize() # Ensure initialized before serving requests

        async with self._lock: # Lock during read/potential refresh
            if force_refresh:
                logger.info("Force refresh requested via get_cached.")
                await self.refresh(force=True) # Force full refresh
            else:
                # Check if cache is stale
                is_stale = True # Default to stale if no timestamp
                if self._cache.get("last_updated"):
                    try:
                        last_update_time = datetime.fromisoformat(self._cache["last_updated"])
                        stale_delta = timedelta(seconds=STALE_THRESHOLD_SECONDS)
                        if datetime.now(timezone.utc) - last_update_time < stale_delta:
                            is_stale = False
                    except ValueError:
                        logger.error("Invalid last_updated timestamp in cache, considering stale.")

                if is_stale:
                    logger.warning("Cache is considered stale. Triggering incremental refresh.")
                    await self.refresh(force=False) # Incremental refresh

            # Return a copy to prevent external modification
            # Ensure changelogs is always a list
            changelogs_list = self._cache.get("changelogs", [])
            if not isinstance(changelogs_list, list):
                logger.error("Cache contains non-list 'changelogs', returning empty list.")
                changelogs_list = []
        
        return {
                 "changelogs": list(changelogs_list), # Return a copy
                 "total": len(changelogs_list),
                 "last_updated": self._cache.get("last_updated")
             }

    def clear_cache(self) -> bool:
        """Clears the in-memory cache and deletes the cache file."""
        # This function might be called from sync context (e.g., admin endpoint)
        # but file deletion should ideally be async. However, for simplicity...
        # Let's make it an async function to use the lock and aiofiles.
        async def _clear():
            async with self._lock:
                 logger.warning("Clearing changelog cache...")
                 self._cache = {"changelogs": [], "last_updated": None, "version": 2}
                 try:
                     if os.path.exists(CACHE_FILE):
                         await aiofiles.os.remove(CACHE_FILE)
                         logger.info(f"Cache file '{CACHE_FILE}' deleted.")
                     return True
                 except Exception as e:
                     logger.error(f"Error deleting cache file '{CACHE_FILE}': {e}")
                     return False
        # If called from sync, need to run it in the loop. Assume called from async context for now.
        # return asyncio.run(_clear()) # This blocks - avoid if possible.
        # Better: Call this from an async route handler.
        logger.warning("Cache clear called - ensure this is run within an async context.")
        # For now, return NotImplementedError if we can't guarantee async context easily.
        # Or, make the endpoint handler run it: await cache_manager.clear_cache_async()
        raise NotImplementedError("clear_cache should be called via async wrapper")

    async def clear_cache_async(self) -> bool:
         """Async version of clearing the cache."""
         async with self._lock:
             logger.warning("Clearing changelog cache...")
             self._cache = {"changelogs": [], "last_updated": None, "version": 2}
             try:
                 if os.path.exists(CACHE_FILE):
                     await aiofiles.os.remove(CACHE_FILE)
                     logger.info(f"Cache file '{CACHE_FILE}' deleted.")
                 return True
             except Exception as e:
                 logger.error(f"Error deleting cache file '{CACHE_FILE}': {e}")
                 return False
            
    def deduplicate_cache(self, save_after=True) -> Dict[str, Any]:
        """
        Synchronous stub for deduplicate_cache. Raises NotImplementedError.
        Use deduplicate_cache_async instead.
        """
        # This remains to clearly indicate the async version should be used.
        raise NotImplementedError("Use deduplicate_cache_async instead")

    async def deduplicate_cache_internal(self, save_after_dedupe: bool = True) -> Dict[str, Any]:
        """Internal deduplication logic. ASSUMES LOCK IS HELD."""
        logger.debug("--- Executing internal deduplication ---")
        original_count = len(self._cache.get("changelogs", []))
        if original_count == 0:
            logger.info("Cache is empty, no deduplication needed.")
            return {"status": "success", "message": "Cache already empty.", "original_count": 0, "removed_count": 0, "final_count": 0}

        seen_ids = set()
        unique_changelogs = []
        duplicates_found = 0

        # Iterate and keep only the first occurrence of each ID
        # Assume cache is sorted newest first; keep the first seen (newest)
        for entry in self._cache.get("changelogs", []):
            entry_id = entry.get("id")
            if entry_id and entry_id not in seen_ids:
                unique_changelogs.append(entry)
                seen_ids.add(entry_id)
            elif entry_id:
                duplicates_found += 1
            else:
                 logger.warning("Found cache entry with missing ID during deduplication.")
                 unique_changelogs.append(entry) # Keep entries without ID? Or discard? Keep for now.

        if duplicates_found > 0:
            logger.info(f"Removed {duplicates_found} duplicate entries during internal dedupe.")
            self._cache["changelogs"] = unique_changelogs
            self._cache["last_updated"] = datetime.now(timezone.utc).isoformat()
            if save_after_dedupe:
                 # *** Call INTERNAL save method ***
                 await self._save_cache_to_file_internal() # Already holds lock
                 logger.debug("Cache saved after internal deduplication.")
            else:
                 logger.debug("Skipping save after deduplication as requested.")

            final_count = len(unique_changelogs)
            return {
                "status": "success",
                "message": f"Removed {duplicates_found} duplicates.",
                "original_count": original_count,
                "removed_count": duplicates_found,
                "final_count": final_count
            }
        else:
            logger.info("No duplicate entries found during internal dedupe.")
            return {
                "status": "success",
                "message": "No duplicates found.",
                "original_count": original_count,
                "removed_count": 0,
                "final_count": original_count
            }

    async def deduplicate_cache_public_safe(self, save_after_dedupe: bool = True) -> Dict[str, Any]:
        """Public method to deduplicate cache, acquiring the lock."""
        logger.info("--- Public dedupe request: Attempting lock ---")
        async with self._lock:
             logger.debug("--- Public dedupe request: Lock acquired ---")
             result = await self._deduplicate_cache_internal(save_after_dedupe=save_after_dedupe)
             logger.debug("--- Public dedupe request: Lock released ---")
             return result

    def get_cache_stats(self) -> Dict[str, Any]:
        """Returns statistics about the current cache state."""
        # No need for lock for simple read if data types are atomic/simple
        # But reading list length and timestamp together is safer with lock
        # Let's make it async to use the lock properly.
        # async def _get_stats():
        #      async with self._lock:
        #           # ... rest of the logic ...
        # raise NotImplementedError("Use get_cache_stats_async")
        # --- OR --- Allow sync read but accept potential minor inconsistency ---
        changelogs = self._cache.get("changelogs", [])
        count = len(changelogs) if isinstance(changelogs, list) else 0
        last_updated = self._cache.get("last_updated")
        is_stale = True
        if last_updated:
             try:
                  update_time = datetime.fromisoformat(last_updated)
                  if datetime.now(timezone.utc) - update_time < timedelta(seconds=STALE_THRESHOLD_SECONDS):
                       is_stale = False
             except ValueError: pass # Invalid format means stale

        return {
            "entry_count": count,
            "last_updated_timestamp": last_updated,
            "is_stale": is_stale,
            "cache_file": CACHE_FILE,
            "refresh_interval_seconds": REFRESH_INTERVAL_SECONDS,
            "stale_threshold_seconds": STALE_THRESHOLD_SECONDS,
            "cache_format_version": self._cache.get("version", "unknown")
        }

    async def _periodic_refresh_loop(self):
        """The background task loop for periodic cache refreshes."""
        if not self._is_initialized:
             logger.error("Periodic refresh loop started before cache manager was initialized. Stopping loop.")
             return

        logger.info(f"Starting periodic cache refresh loop (interval: {REFRESH_INTERVAL_SECONDS}s)")
        while True:
            try:
                await asyncio.sleep(REFRESH_INTERVAL_SECONDS)
                logger.info("Periodic refresh triggered.")
                await self.refresh(force=False)
            except asyncio.CancelledError:
                logger.info("Periodic refresh task cancelled.")
                break
            except Exception as e:
                logger.error(f"Error in periodic refresh loop: {e}")
                logger.debug(traceback.format_exc())
                # Avoid rapid failure loops - sleep for a shorter duration before retrying?
                await asyncio.sleep(60) # Sleep 1 minute after error before next cycle

    async def start_periodic_refresh(self):
        """Starts the background task for periodic cache refreshes."""
        if self._periodic_refresh_task and not self._periodic_refresh_task.done():
            logger.warning("Periodic refresh task already running.")
            return

        if not self._get_changelog_func:
             logger.error("Cannot start periodic refresh: get_changelog function not registered.")
             return

        # Create and store the task
        self._periodic_refresh_task = asyncio.create_task(self._periodic_refresh_loop())
        logger.info("Periodic cache refresh task started.")

    async def stop_periodic_refresh(self):
        """Stops the background task for periodic cache refreshes."""
        if self._periodic_refresh_task and not self._periodic_refresh_task.done():
            logger.info("Stopping periodic cache refresh task...")
            self._periodic_refresh_task.cancel()
            try:
                await self._periodic_refresh_task
            except asyncio.CancelledError:
                logger.info("Periodic refresh task successfully stopped.")
            self._periodic_refresh_task = None
        else:
            logger.info("Periodic refresh task not running or already stopped.")

# Singleton instance of the cache manager
cache_manager = ChangelogCacheManager() 