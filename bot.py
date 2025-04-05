import asyncio
import sys
import logging # Logging is configured in config.py
import discord

# Import components
import config # Initializes logging and loads env vars
import discord_bot
import api
import wiki_integration # Import even if not directly called in main, maybe for future use
from changelog_cache import cache_manager

# Use the configured logger
logger = logging.getLogger(__name__)

async def main():
    """Main function to initialize and run the bot and API."""
    logger.info("=== Application Starting ===")
    logger.info("") # Add newline

    try:
        # Environment variables are checked in config.py upon import

        # --- Discord Bot ---
        logger.info("--- Starting Discord Bot ---")
        logger.info("Creating Discord client task...")
        discord_task = asyncio.create_task(discord_bot.start_discord(), name="DiscordBotTask")

        logger.info("Waiting for Discord client to connect and be ready...")
        try:
            await asyncio.wait_for(discord_bot.wait_until_ready(), timeout=60.0)
            logger.info("✅ Discord client is ready!")
        except asyncio.TimeoutError:
            logger.critical("❌ Discord client failed to become ready within 60 seconds. Shutting down.")
            # Attempt to cancel the discord task cleanly
            discord_task.cancel()
            try:
                await discord_task
            except asyncio.CancelledError:
                pass
            return # Exit main function
        logger.info("") # Add newline

        # --- Cache Manager ---
        logger.info("--- Initializing Cache Manager ---")
        # Check if essential channels were found (logged in discord_bot.on_ready)
        if not discord_bot.get_changelog_channel():
             logger.error("❌ Essential changelog channel not found. API functionality might be limited.")
             # Decide whether to continue or exit based on severity
             # For now, continue but log error.

        # Register the get_changelog function from the api module
        if api.get_changelog:
            logger.info("Registering API's get_changelog function with Cache Manager...")
            cache_manager.register_get_changelog_func(api.get_changelog)
        else:
             logger.error("❌ Could not find get_changelog function in api module to register.")
             # This is critical for cache refreshes, maybe exit?
             return

        logger.info("Initializing Changelog Cache Manager (loading from file, initial refresh)...")
        # Initialize performs load and initial refresh check
        await cache_manager.initialize()
        logger.info("✅ Cache Manager initialized.")
        logger.info("") # Add newline

        # --- Periodic Tasks ---
        logger.info("--- Starting Background Tasks ---")
        logger.info("Starting periodic cache refresh background task...")
        # The start function now resides within the cache_manager instance
        await cache_manager.start_periodic_refresh()
        cache_task = cache_manager._periodic_refresh_task # Get ref if needed later
        logger.info("✅ Periodic cache refresh task started.")
        logger.info("") # Add newline

        # --- API Server ---
        logger.info("--- Starting API Server ---")
        logger.info("Creating FastAPI server task...")
        api_task = asyncio.create_task(api.start_api(), name="FastAPITask")
        # Note: FastAPI/Uvicorn will log its own startup messages after this point.
        logger.info("") # Add newline

        # --- Running State ---
        logger.info("--- Running Concurrently ---")
        logger.info("🚀 Bot and API are running concurrently. Monitoring tasks...")
        # Gather the main tasks. The periodic refresh runs in the background managed by cache_manager.
        # We might want to add cache_task here if we need to explicitly await its completion on shutdown.
        tasks_to_await = [discord_task, api_task]
        if cache_task:
            tasks_to_await.append(cache_task) # Ensure clean shutdown of cache task too

        done, pending = await asyncio.wait(tasks_to_await, return_when=asyncio.FIRST_COMPLETED)

        # If a task finishes (or fails), log it and potentially stop others
        for task in done:
            try:
                result = task.result()
                logger.warning(f"Task {task.get_name()} finished unexpectedly with result: {result}")
            except Exception as e:
                logger.error(f"Task {task.get_name()} failed with exception:", exc_info=e)

        logger.warning("\n--- Initiating Shutdown ---") # Add newline before shutdown message
        # Cancel pending tasks for clean shutdown
        for task in pending:
             logger.info(f"Cancelling task {task.get_name()}...")
             task.cancel()

        # Await cancellation
        await asyncio.gather(*pending, return_exceptions=True)
        logger.info("All tasks cancelled.")


    except ValueError as e:
        # Catch config errors from config.check_environment_variables()
        logger.critical(f"❌ Configuration Error: {e}")
        sys.exit(1) # Exit if config is bad
    except discord.LoginFailure:
         logger.critical("❌ Discord Login Failed during startup.")
         # No need to exit here, start_discord should raise it, caught by general Exception
    except Exception as e:
        logger.critical(f"❌ An unexpected error occurred during application startup or main loop: {type(e).__name__}")
        logger.critical(f"Error details: {e}", exc_info=True)
        # Attempt clean shutdown of background tasks if they exist
        if 'cache_manager' in locals() and cache_manager._periodic_refresh_task:
             await cache_manager.stop_periodic_refresh()
        # Other cleanup if necessary
        sys.exit(1) # Exit on critical error

    finally:
        logger.info("\n=== Application Shutting Down ===") # Add newline before final shutdown block
        # Ensure cache periodic refresh is stopped cleanly if it was started
        if 'cache_manager' in locals() and cache_manager._periodic_refresh_task:
            await cache_manager.stop_periodic_refresh()

        # Close Discord client connection if it's running
        if 'discord_bot' in locals() and discord_bot.is_ready():
            logger.info("Closing Discord client connection...")
            await discord_bot.client.close()
            logger.info("Discord client closed.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info(" Shutdown requested via KeyboardInterrupt.")
    except Exception as e:
         # Catch errors that might occur even before the main loop starts properly
         logging.critical(f"❌ Critical error outside main loop: {e}", exc_info=True)
         sys.exit(1)
    finally:
         logging.info(" Main execution finished.") 