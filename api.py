import discord # Keep discord import if using discord objects directly
from fastapi import FastAPI, HTTPException, Security, Depends
from fastapi.security import APIKeyHeader
import aiohttp
from typing import Optional
from datetime import datetime
import uvicorn
import logging
import traceback

# Import config, discord bot client/helpers, wiki helpers, cache manager
from config import PATCHER_TOKEN, PORT, WIKI_PAGE_ID, logger
import discord_bot
import wiki_integration
from changelog_cache import cache_manager

# --- FastAPI Setup ---
app = FastAPI(
    title="THJ Discord Bot API",
    description="API for interacting with the THJ Discord Bot and related services.",
    version="1.0.0"
)

# --- Security ---
api_key_header = APIKeyHeader(name="X-Patcher-Token", auto_error=True)

async def verify_token(api_key: str = Security(api_key_header)):
    """Verify the API token provided in the X-Patcher-Token header."""
    if api_key != PATCHER_TOKEN:
        logger.warning("Unauthorized API access attempt detected.")
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing authentication token"
        )
    return api_key

# --- API Endpoints ---

# --- Health/Status Endpoint ---
@app.get("/health", tags=["Status"])
async def health_check():
    """Check the health of the API and connection to Discord."""
    discord_ready = discord_bot.is_ready()
    status_code = 200 if discord_ready else 503
    return {"status": "ok" if discord_ready else "error", "discord_ready": discord_ready, "status_code": status_code}


# --- Changelog Endpoints ---
@app.get("/changelog/{message_id}", dependencies=[Depends(verify_token)], tags=["Changelog"])
@app.get("/changelog", dependencies=[Depends(verify_token)], tags=["Changelog"])
async def get_changelog(
    message_id: Optional[str] = None,
    all: Optional[bool] = False,
    limit: Optional[int] = None,
    is_cache_refresh: bool = False
):
    """
    Get changelogs from the Discord channel.
    Accepts optional 'limit' for fetching history.

    - `/changelog`: Get the latest changelog.
    - `/changelog?all=true`: Get all cached/available changelogs.
    - `/changelog/{message_id}`: Get changelogs newer than the specified message ID.
    - `/changelog?message_id=...`: Get changelogs newer than the specified message ID.

    Requires `X-Patcher-Token` header. Internal use allows `is_cache_refresh=true` to bypass cache checks and reduce logging.
    """
    # Dependency checks moved inside endpoint for clarity
    if not discord_bot.is_ready():
        logger.error("get_changelog endpoint called while Discord client is not ready.")
        raise HTTPException(status_code=503, detail="Discord client is not ready")

    changelog_channel = discord_bot.get_changelog_channel()
    if not changelog_channel:
        logger.error("get_changelog endpoint called but changelog channel is not found.")
        raise HTTPException(status_code=503, detail="Changelog channel not found or initialized")

    # Log summary includes limit now if provided by cache manager
    log_summary = f"msg_id={message_id}, all={all}, limit={limit}, cache_refresh={is_cache_refresh}"
    if not is_cache_refresh:
        logger.info(f"Changelog request received: {log_summary}")

    # Cache Check (only for 'all=true' and non-refresh calls)
    if all and not message_id and not is_cache_refresh:
        logger.info("Handling 'all=true' request, checking cache first.")
        cache_result = await cache_manager.get_cached(force_refresh=False) # Don't force refresh here
        if cache_result and cache_result.get("changelogs"):
            logger.info(f"Returning {cache_result['total']} cached changelogs (last updated: {cache_result['last_updated']})")
            return {
                "status": "success",
                "source": "cache",
                "changelogs": cache_result["changelogs"],
                "total": cache_result["total"],
                "last_updated": cache_result["last_updated"]
            }
        else:
            logger.info("Cache miss or empty for 'all=true', proceeding with direct fetch.")
            # Continue to fetch directly if cache is empty/stale


    # Direct Fetch Logic
    messages_data = []
    # Use the passed limit, default to None if not provided
    fetch_limit = limit

    try:
        if message_id:
            # Fetch messages *after* a specific ID
            try:
                reference_message = discord.Object(id=int(message_id))
                if not is_cache_refresh:
                    # Use the explicit fetch_limit requested by cache manager if available
                    logger.debug(f"Fetching messages after ID: {message_id} (limit={fetch_limit or 'discord default'})")
                # Pass the fetch_limit to history()
                async for message in changelog_channel.history(limit=fetch_limit, after=reference_message): # Use fetch_limit
                    if '```' in message.content: # Simple changelog check
                        messages_data.append({
                            "id": str(message.id),
                            "content": message.content,
                            "author": str(message.author), # Use consistent author format
                            "timestamp": message.created_at.isoformat()
                        })
                if not is_cache_refresh:
                    logger.info(f"Found {len(messages_data)} new messages after ID {message_id}")
            except ValueError:
                logger.error(f"Invalid message_id format: {message_id}")
                raise HTTPException(status_code=400, detail="Invalid message ID format")
            except discord.NotFound:
                 logger.warning(f"Reference message ID {message_id} not found.")
                 # Decide how to handle: error or return empty? Returning empty is safer.
                 messages_data = []
            except discord.Forbidden:
                 logger.error(f"Permission error fetching history after ID {message_id}.")
                 raise HTTPException(status_code=500, detail="Permission error fetching messages")
            except Exception as e:
                 logger.error(f"Error fetching messages after ID {message_id}: {e}")
                 raise HTTPException(status_code=500, detail=f"Error fetching messages: {e}")

        elif all:
            # Fetch all messages (or up to a limit for cache refresh)
            log_prefix = "Fetching all changelogs"
            if is_cache_refresh:
                # If cache refresh calls with all=True, respect its limit preference if any
                fetch_limit = limit if limit is not None else 1000 # Default limit for cache refresh 'all'
                log_prefix = f"Fetching up to {fetch_limit} changelogs for cache refresh"
                logger.debug(log_prefix)
            else:
                 # Direct API call for all=true (cache miss scenario)
                 # Allow specifying limit via query param? For now, use a high default or None.
                 fetch_limit = limit if limit is not None else 2000 # Default limit for direct 'all' request
                 log_prefix = f"Fetching up to {fetch_limit} changelogs directly"
                 logger.info(log_prefix)

            async for message in changelog_channel.history(limit=fetch_limit): # Use fetch_limit
                 if '```' in message.content:
                    messages_data.append({
                        "id": str(message.id),
                        "content": message.content,
                        "author": str(message.author),
                        "timestamp": message.created_at.isoformat()
                    })
            if not is_cache_refresh:
                logger.info(f"Fetched {len(messages_data)} total messages directly.")

        else:
            # Fetch the latest single changelog
            # Limit is less relevant here, but we respect it if passed (unlikely)
            fetch_limit = limit if limit is not None else 20 # Default lookback for latest
            if not is_cache_refresh:
                logger.debug(f"Fetching the latest changelog (checking last {fetch_limit} messages).")
            async for message in changelog_channel.history(limit=fetch_limit): # Use fetch_limit
                 if '```' in message.content:
                      messages_data.append({
                        "id": str(message.id),
                        "content": message.content,
                        "author": str(message.author),
                        "timestamp": message.created_at.isoformat()
                      })
                      break # Found the latest one
            if not is_cache_refresh:
                 logger.info(f"Found latest changelog: ID {messages_data[0]['id'] if messages_data else 'None'}")

        # Sort messages by ID (important!) - oldest to newest
        messages_data.sort(key=lambda x: int(x["id"]))

        return {
            "status": "success",
            "source": "direct_fetch",
            "changelogs": messages_data,
            "total": len(messages_data)
        }

    except HTTPException: # Re-raise HTTP exceptions
        raise
    except Exception as e:
        logger.error(f"Error processing changelog request ({log_summary}): {e}")
        logger.debug(traceback.format_exc()) # Log traceback for debugging
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")


# --- Patcher Specific Endpoints (Simplified Changelog Access) ---
@app.get("/patcher/latest", dependencies=[Depends(verify_token)], tags=["Patcher"])
async def get_latest_for_patcher():
    """
    Secure endpoint for the patcher to get the very latest changelog entry.
    Formats the content similar to the wiki entry format.
    Requires `X-Patcher-Token` header.
    """
    logger.info("Patcher requesting latest changelog.")
    # Use the main get_changelog function to get the latest
    latest_changelog_response = await get_changelog(message_id=None, all=False)

    if latest_changelog_response["total"] == 0:
        logger.info("No changelog entries found for patcher.")
        return {
            "status": "success",
            "found": False,
            "message": "No changelog entries found"
        }

    # Get the single latest message from the response
    last_message_data = latest_changelog_response["changelogs"][0]

    # Format it for the patcher (similar to wiki but maybe simplified)
    # Use the wiki formatter for consistency
    try:
        timestamp = datetime.fromisoformat(last_message_data["timestamp"])
        formatted_content = wiki_integration.format_changelog_for_wiki(
            last_message_data["content"],
            timestamp,
            last_message_data["author"] # Assuming author is already stringified
        )
    except Exception as fmt_e:
        logger.error(f"Error formatting changelog for patcher: {fmt_e}")
        formatted_content = f"Error formatting content: {last_message_data['content']}" # Fallback

    return {
        "status": "success",
        "found": True,
        "changelog": {
            "raw_content": last_message_data["content"],
            "formatted_content": formatted_content, # Provide formatted version
            "author": last_message_data["author"],
            "timestamp": last_message_data["timestamp"],
            "message_id": last_message_data["id"]
        }
    }

# --- Wiki Update Endpoints ---
@app.post("/wiki/process-latest", dependencies=[Depends(verify_token)], tags=["Wiki"])
async def process_latest_changelog_and_update_wiki():
    """
    Fetches the latest changelog message from Discord, formats it,
    and updates the configured Wiki page if it's newer than the content already there.
    Requires `X-Patcher-Token` header.
    """
    logger.info("Received request to process latest changelog and update wiki.")

    if not all([wiki_integration.WIKI_API_URL, wiki_integration.WIKI_API_KEY, wiki_integration.WIKI_PAGE_ID]):
        logger.error("Wiki integration is not fully configured for /wiki/process-latest endpoint.")
        raise HTTPException(status_code=501, detail="Wiki integration not configured")

    # 1. Get the latest changelog entry
    latest_changelog_response = await get_changelog(message_id=None, all=False)
    if latest_changelog_response["total"] == 0:
        logger.info("No changelog entries found to process for wiki update.")
        return {"status": "success", "message": "No new changelog entries found"}

    message_data = latest_changelog_response["changelogs"][0]
    message_id = message_data["id"]
    message_content = message_data["content"]
    message_author = message_data["author"]
    try:
        message_timestamp = datetime.fromisoformat(message_data["timestamp"])
    except ValueError:
        logger.error(f"Invalid timestamp format for message {message_id}: {message_data['timestamp']}")
        message_timestamp = datetime.utcnow() # Fallback, though should not happen

    # 2. Format the new entry
    new_entry_formatted = wiki_integration.format_changelog_for_wiki(
        message_content, message_timestamp, message_author
    )
    if not new_entry_formatted:
         logger.error(f"Failed to format message {message_id} for wiki.")
         raise HTTPException(status_code=500, detail=f"Failed to format message {message_id}")

    # 3. Get current wiki content
    current_wiki_content = await wiki_integration.get_wiki_content(WIKI_PAGE_ID)
    if current_wiki_content is None: # Indicates an error fetching
        raise HTTPException(status_code=503, detail="Failed to retrieve current wiki content")

    # 4. Check if this entry (or similar) is already present
    # Simple check: Look for the formatted date and author line
    entry_header_check = f"# {message_timestamp.strftime('%B %d, %Y')}\n## {message_author}"
    if entry_header_check in current_wiki_content:
         # More robust check: Compare content snippet if header matches
         if message_content.replace('```', '').strip()[:100] in current_wiki_content:
            logger.info(f"Latest changelog entry (ID: {message_id}) seems to already be in the Wiki. Skipping update.")
            return {
                "status": "success",
                "message": f"Changelog entry {message_id} already present in Wiki.",
                "updated": False
            }

    # 5. Process and combine content (add new entry to the top)
    full_new_content = await wiki_integration.process_wiki_content(current_wiki_content, new_entry_formatted)

    # 6. Update the wiki page
    success = await wiki_integration.update_wiki_page(full_new_content, WIKI_PAGE_ID)

    if success:
        logger.info(f"✅ Successfully updated Wiki with latest changelog (ID: {message_id})")
        # Update cache as well? The on_message handler should ideally do this.
        # Or we can add it here for redundancy if needed.
        cache_manager.add_single_changelog(message_data)

        return {
            "status": "success",
            "message": f"Successfully processed and updated wiki with changelog ID: {message_id}",
            "updated": True,
            "changelog": message_data # Return the data of the entry added
        }
    else:
        logger.error(f"❌ Failed to update Wiki with latest changelog (ID: {message_id})")
        raise HTTPException(status_code=500, detail="Failed to update Wiki page")


# Note: Removed /wiki/update-changelog (full update) as it's less common and covered by cache + process-latest
# If needed, it can be added back, fetching all from cache/discord and bulk-formatting.

# --- Value/EXP Boost Endpoints ---
# Note: The original /value endpoint seemed unused or duplicated by /expbonus logic.
# Let's keep /expbonus which reads the channel *name*.

@app.get("/expbonus", dependencies=[Depends(verify_token)], tags=["EXP Boost"])
async def get_exp_boost():
    """
    Get the current EXP boost value by reading the name of the configured EXP Boost channel.
    Requires `X-Patcher-Token` header.
    """
    logger.info("Request received for EXP boost value.")
    if not discord_bot.is_ready():
        raise HTTPException(status_code=503, detail="Discord client is not ready")

    exp_boost_channel = discord_bot.get_exp_boost_channel()
    if not exp_boost_channel:
        # Check if it was configured at all
        if discord_bot.EXP_BOOST_CHANNEL_ID:
             logger.warning("EXP Boost channel configured but not found by the bot.")
             raise HTTPException(status_code=503, detail="EXP boost channel configured but not found")
        else:
             logger.info("EXP Boost functionality is not configured.")
             raise HTTPException(status_code=404, detail="EXP boost functionality is not configured")

    logger.info(f"Found EXP boost channel: #{exp_boost_channel.name}")
    # The value is assumed to be the channel's name
    exp_boost_value = exp_boost_channel.name

    return {
        "status": "success",
        "found": True,
        "exp_boost": exp_boost_value,
        "channel_id": str(exp_boost_channel.id),
        "channel_name": exp_boost_channel.name, # Explicitly return name too
         "last_checked": datetime.utcnow().isoformat() # Indicate when checked
    }

# --- Server Status Endpoint ---
@app.get("/serverstatus", dependencies=[Depends(verify_token)], tags=["Server Status"])
async def get_server_status():
    """
    Get the current server status (player count) from the Project EQ API via a proxy.
    Requires `X-Patcher-Token` header.
    """
    logger.info("Fetching server status from Project EQ API.")
    # Use the same proxy URL as before
    proxy_url = "https://api.codetabs.com/v1/proxy?quest=http://login.projecteq.net/servers/list"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(proxy_url, timeout=10) as response: # Add timeout
                if response.status != 200:
                    logger.error(f"Failed to fetch server status from proxy. Status: {response.status}")
                    raise HTTPException(status_code=response.status, detail="Failed to fetch server status from proxy")

                data = await response.json()
                logger.debug("Successfully fetched server data from proxy.")

                # Find the specific server (adjust name if needed)
                target_server_name_part = "Heroes' Journey [Multiclass"
                server_info = next(
                    (s for s in data if target_server_name_part in s.get('server_long_name', '')),
                    None
                )

                if not server_info:
                    logger.warning(f"Server containing '{target_server_name_part}' not found in API response.")
                    return {
                        "status": "success",
                        "found": False,
                        "message": f"Server '{target_server_name_part}' not found in API response"
                    }

                players_online = server_info.get('players_online', 'N/A') # Default if key missing
                server_name = server_info.get('server_long_name', 'Unknown Name')

                logger.info(f"Found server: {server_name}, Players Online: {players_online}")
                return {
                    "status": "success",
                    "found": True,
                    "server": {
                        "name": server_name,
                        "players_online": players_online,
                        "last_updated": datetime.utcnow().isoformat()
                    }
                }

    except asyncio.TimeoutError:
         logger.error("Timeout error fetching server status from proxy.")
         raise HTTPException(status_code=504, detail="Timeout fetching server status from proxy")
    except aiohttp.ClientError as e:
        logger.error(f"Network error fetching server status: {e}")
        raise HTTPException(status_code=503, detail="Failed to connect to server status proxy")
    except json.JSONDecodeError:
         logger.error("Error decoding JSON response from server status proxy.")
         raise HTTPException(status_code=500, detail="Invalid response format from server status proxy")
    except Exception as e:
        logger.error(f"Unexpected error fetching server status: {e}")
        logger.debug(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")


# --- Admin/Cache Endpoints ---
@app.get("/admin/cache-stats", dependencies=[Depends(verify_token)], tags=["Admin"])
async def get_cache_stats(clear: Optional[bool] = False, force_refresh: Optional[bool] = False):
    """
    Get cache statistics. Optional actions: `clear=true` or `force_refresh=true`.
    Requires `X-Patcher-Token` header.
    """
    logger.info(f"Admin request for cache stats (clear={clear}, force_refresh={force_refresh})")

    action_results = {"cache_cleared": False, "cache_refreshed": False, "refresh_count": None}

    try:
        if clear:
            logger.warning("⚠️ Admin executing cache clear")
            result = cache_manager.clear_cache()
            action_results["cache_cleared"] = result
            logger.info(f"Cache clear result: {'Success' if result else 'Failed'}")

        if force_refresh:
            logger.info("🔄 Admin executing force refresh of cache")
            # Call refresh method which now uses the registered get_changelog
            refresh_count = await cache_manager.refresh(force=True)
            action_results["cache_refreshed"] = refresh_count is not None
            action_results["refresh_count"] = refresh_count
            logger.info(f"Cache force refresh result: {'Success' if action_results['cache_refreshed'] else 'Failed'}. Count: {refresh_count}")

        stats = cache_manager.get_cache_stats()
        logger.debug(f"Returning cache stats: {stats}")

        return {
            "status": "success",
            "cache_stats": stats,
            "actions": action_results
        }

    except Exception as e:
        logger.error(f"Error in admin/cache-stats endpoint: {e}")
        logger.debug(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Error processing cache admin request: {e}")


@app.get("/admin/deduplicate-cache", dependencies=[Depends(verify_token)], tags=["Admin"])
async def deduplicate_cache():
    """
    Remove duplicate entries from the changelog cache based on message ID.
    Refreshes the cache after deduplication if duplicates were removed.
    Requires `X-Patcher-Token` header.
    """
    logger.info("Admin request to deduplicate cache.")
    try:
        result = cache_manager.deduplicate_cache()
        removed_count = result.get("removed_count", 0)
        message = result.get("message", "Deduplication process completed.")

        if result.get("status") == "success":
             logger.info(message)
             final_stats = cache_manager.get_cache_stats() # Get stats after deduplication

             # Optionally refresh if duplicates were found and removed
             if removed_count > 0:
                 logger.info(f"Removed {removed_count} duplicates. Performing validation refresh.")
                 await cache_manager.refresh(force=True)
                 final_stats = cache_manager.get_cache_stats() # Get stats after potential refresh

             return {
                "status": "success",
                "message": message,
                "deduplication_stats": result,
                "final_cache_stats": final_stats
            }
        else:
            logger.error(f"Cache deduplication failed: {message}")
            raise HTTPException(status_code=500, detail=f"Cache deduplication failed: {message}")

    except Exception as e:
        logger.error(f"Error during cache deduplication: {e}")
        logger.debug(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Error during cache deduplication: {e}")


# --- Server Start Function ---
async def start_api():
    """Configure and start the Uvicorn server for the FastAPI app."""
    try:
        logger.info(f"🚀 Starting FastAPI server on host 0.0.0.0:{PORT}...")
        config = uvicorn.Config(
            app="api:app", # Point to the app object in this file
            host="0.0.0.0",
            port=PORT,
            log_level="info", # Uvicorn's own logging level
            reload=False # Disable auto-reload for production/docker
        )
        server = uvicorn.Server(config)
        await server.serve()
    except Exception as e:
        logger.critical(f"❌ Failed to start FastAPI server: {e}")
        logger.debug(traceback.format_exc())
        raise # Re-raise critical error 