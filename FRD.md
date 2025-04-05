# FRD - Functional Requirements Document

## Project Overview

This project consists of a Discord bot and a FastAPI server designed to monitor a specific Discord channel for changelog messages, cache them, and provide them via a secure API. It also includes functionality for interacting with a Wiki.js instance and retrieving other specific data points from Discord channels.

## Core Components

1.  **Discord Bot (`bot.py`)**:
    *   Connects to Discord using `discord.py`.
    *   Identifies the target changelog channel (`CHANGELOG_CHANNEL_ID`) and optional exp boost channel (`EXP_BOOST_CHANNEL_ID`).
    *   Provides the underlying connection and message fetching capabilities.

2.  **FastAPI Server (`bot.py`)**:
    *   Runs alongside the Discord bot in the same process using `asyncio`.
    *   Exposes secure API endpoints using FastAPI.
    *   Requires an `X-Patcher-Token` header for authentication on most endpoints.
    *   Serves cached changelogs and other data.

3.  **Changelog Cache (`changelog_cache.py`)**:
    *   Manages caching of changelog messages to a JSON file (`changelog_cache.json`).
    *   Uses an in-memory layer to reduce disk I/O.
    *   Provides methods for loading, saving, validating, and refreshing the cache.
    *   **Event-Driven Updates**: Uses the `on_message` Discord event to add new changelogs to the cache almost instantly when they are posted in the `CHANGELOG_CHANNEL_ID`.
    *   **Periodic Refresh (Backup)**: Includes automated periodic cache refreshes (default: 30 seconds) performing incremental updates with lookback as a fallback/consistency check.
    *   Performs an initial full refresh on startup.
    *   Includes logic for deduplicating entries during refreshes and adds.
    *   **Incremental Refresh Lookback**: Uses a lookback mechanism during incremental refreshes. It fetches messages after the ID that is `INCREMENTAL_REFRESH_LOOKBACK` entries older than the newest cached message, providing a safety margin. Defaults to 5.
    *   Throttles disk writes to avoid excessive I/O (default: min 60s between writes, but forced for `on_message` additions).
    *   Limits the maximum number of entries stored in the cache (default: 1000).

## Configuration (`.env`)

*   `DISCORD_TOKEN`: (Required) The Discord bot token.
*   `CHANGELOG_CHANNEL_ID`: (Required) The ID of the Discord channel containing changelogs.
*   `PATCHER_TOKEN`: (Required) The secret token for API authentication.
*   `EXP_BOOST_CHANNEL_ID`: (Optional) The ID of the channel used for the exp boost value (reads channel name).
*   `WIKI_API_URL`: (Optional) URL for the Wiki.js GraphQL API.
*   `WIKI_API_KEY`: (Optional) API key for Wiki.js.
*   `WIKI_PAGE_ID`: (Optional) The ID of the Wiki.js page to update.
*   `PORT`: (Optional) Port for the FastAPI server (defaults to 80).

## API Endpoints

*   **`GET /changelog`**:
    *   Requires `X-Patcher-Token`.
    *   Returns the latest changelog entry from the cache.
*   **`GET /changelog?all=true`**:
    *   Requires `X-Patcher-Token`.
    *   Returns all available changelogs from the cache.
*   **`GET /changelog/{message_id}`**:
    *   Requires `X-Patcher-Token`.
    *   Returns all changelogs *after* the specified `message_id`. Fetches directly from Discord (not cached). *Note: This behavior might differ from the cache's internal fetch.*
*   **`GET /last-message`**:
    *   Requires `X-Patcher-Token`.
    *   Fetches the absolute latest message directly from the changelog channel (not cached).
*   **`GET /patcher/latest`**:
    *   Requires `X-Patcher-Token`.
    *   Fetches the latest changelog message directly and formats it for the patcher.
*   **`GET /value`**:
    *   Requires `X-Patcher-Token`.
    *   Fetches the content of the latest message from the `EXP_BOOST_CHANNEL_ID`.
*   **`GET /expbonus`**:
    *   Requires `X-Patcher-Token`.
    *   Reads the *name* of the `EXP_BOOST_CHANNEL_ID` channel.
*   **`GET /serverstatus`**:
    *   Requires `X-Patcher-Token`.
    *   Fetches server status from an external API (Project EQ).
*   **`GET /admin/cache-stats`**:
    *   Requires `X-Patcher-Token`.
    *   Returns statistics about the changelog cache.
    *   Optional query parameters: `?clear=true` (clears cache), `?force_refresh=true` (triggers full refresh).
*   **`GET /admin/deduplicate-cache`**:
    *   Requires `X-Patcher-Token`.
    *   Removes duplicate entries from the cache file and performs a validation refresh.
*   **`POST /wiki/update-changelog`**:
    *   Requires `X-Patcher-Token`.
    *   Fetches all changelogs and updates the configured Wiki.js page.
*   **`POST /process-latest`**:
    *   Requires `X-Patcher-Token`.
    *   Fetches the latest changelog message, checks if it's already on the Wiki, and updates the Wiki if it's new.

## Cache Logic Details

*   **Initialization**: Loads cache from `changelog_cache.json` into memory. Performs a full refresh.
*   **Real-time Update (`on_message`)**: When a message appears in the target channel, if it looks like a changelog and isn't a duplicate, it's added to the cache immediately via `add_single_changelog`. The cache save is prioritized (`force_write=True`).
*   **Periodic Refresh (Backup)**: Every `ttl_seconds` (30s), performs an *incremental* refresh using the lookback mechanism as a safety net.
*   **Incremental Refresh**: Fetches messages after the ID determined by `INCREMENTAL_REFRESH_LOOKBACK`. Adds only new, unique messages to the cache. Updates `last_message_id` if a genuinely newer message is found.
*   **Full Refresh**: Fetches a capped number of recent messages (e.g., 1000) when triggered (manually or on init). Replaces the cache content with unique entries from the fetch. Updates `last_message_id`.
*   **Deduplication**: All update methods (event, incremental, full) filter out entries with IDs already present in the cache before adding. The `/admin/deduplicate-cache` endpoint cleans the existing file.
*   **Saving**: Updates in-memory cache immediately. Writes to disk are throttled (min 60s interval) unless `force_write=True` is used (e.g., during full refreshes, deduplication, or `on_message` additions).
*   **Serving**: API requests primarily read from the in-memory cache.

## Wiki Integration

*   Uses GraphQL mutations to update and render pages on a Wiki.js instance.
*   Requires `WIKI_API_URL`, `WIKI_API_KEY`, and `WIKI_PAGE_ID` to be set.
*   The `/process-latest` endpoint attempts to add only new entries idempotently.
*   The `/wiki/update-changelog` endpoint overwrites the wiki page with all currently known changelogs.

## Constants

*   `INCREMENTAL_REFRESH_LOOKBACK` (in `changelog_cache.py`): Number of entries to look back for incremental refresh starting point (Default: 5).
*   `CACHE_FETCH_LIMIT` (implied in `get_changelog`): Max messages fetched during a *cache refresh* when `all=True` (Default: 1000).
*   `DISK_WRITE_INTERVAL` (in `changelog_cache.py`): Minimum seconds between disk writes for cache (Default: 60).
*   `CACHE_TTL_SECONDS` (in `changelog_cache.py`): Interval for periodic refreshes (Default: 30).
*   `CACHE_MAX_ENTRIES` (in `changelog_cache.py`): Max entries stored in cache (Default: 1000). 