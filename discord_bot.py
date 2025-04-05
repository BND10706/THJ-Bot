import discord
import logging
import asyncio

# Import specific config variables and logger
from config import DISCORD_TOKEN, CHANGELOG_CHANNEL_ID, EXP_BOOST_CHANNEL_ID, logger
from changelog_cache import cache_manager # Import cache manager

# --- Discord Client Setup ---
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
client = discord.Client(intents=intents)

# --- Global Channel Variables ---
# These will be populated in on_ready
changelog_channel = None
exp_boost_channel = None

# --- Event Handlers ---
@client.event
async def on_ready():
    """Handle Discord client ready event."""
    global changelog_channel, exp_boost_channel
    logger.info(f'🤖 Logged in as {client.user.name} ({client.user.id})')
    logger.info('Searching for configured channels...')

    found_changelog = False
    found_exp_boost = False

    for guild in client.guilds:
        logger.debug(f"Checking guild: {guild.name} ({guild.id})")
        for channel in guild.channels:
            if channel.id == CHANGELOG_CHANNEL_ID:
                changelog_channel = channel
                logger.info(f'✅ Found changelog channel: #{channel.name} ({channel.id}) in guild {guild.name}')
                found_changelog = True
            elif EXP_BOOST_CHANNEL_ID and channel.id == EXP_BOOST_CHANNEL_ID:
                exp_boost_channel = channel
                logger.info(f'✅ Found exp boost channel: #{channel.name} ({channel.id}) in guild {guild.name}')
                found_exp_boost = True

            # Optimization: stop checking channels in this guild if both found
            if found_changelog and (found_exp_boost or not EXP_BOOST_CHANNEL_ID):
                break
        # Optimization: stop checking guilds if both found
        if found_changelog and (found_exp_boost or not EXP_BOOST_CHANNEL_ID):
                break

    if not changelog_channel:
        logger.error(f'❌ Could not find changelog channel with ID: {CHANGELOG_CHANNEL_ID}!')
    if EXP_BOOST_CHANNEL_ID and not exp_boost_channel:
        logger.warning(f'⚠️ Could not find exp boost channel with ID: {EXP_BOOST_CHANNEL_ID} (optional)')
    elif not EXP_BOOST_CHANNEL_ID:
         logger.info("⚪ Exp boost channel ID not configured, skipping search.")

    logger.info('✅ Discord client is ready.')


@client.event
async def on_message(message: discord.Message):
    """Handle messages received by the bot, specifically for changelog updates."""
    # Ignore messages from the bot itself or other bots
    if message.author == client.user or message.author.bot:
        return

    # Check if the message is in the target changelog channel
    if message.channel.id == CHANGELOG_CHANNEL_ID:
        logger.debug(f"Message received in changelog channel: {message.id} by {message.author}")

        # Basic check if it looks like a changelog (must contain ```)
        # This assumes changelogs are always formatted with code blocks
        if '```' in message.content:
            logger.info(f"Potential new changelog detected via on_message in channel {CHANGELOG_CHANNEL_ID}: ID {message.id}")
            # Format the message data similar to how get_changelog does
            # Ensure author is represented consistently (e.g., name + discriminator or display_name)
            message_data = {
                "id": str(message.id),
                "content": message.content,
                "author": str(message.author), # Or message.author.display_name
                "timestamp": message.created_at.isoformat()
            }
            # Add it to the cache
            added = cache_manager.add_single_changelog(message_data)
            if added:
                 logger.info(f"Successfully added message {message.id} to cache via on_message.")
                 # Optional: Trigger wiki update here if desired for real-time updates
                 # await trigger_wiki_update(message_data) # Example
            else:
                 logger.info(f"Message {message.id} was not added to cache via on_message (likely duplicate or error).")
        else:
             logger.debug(f"Message {message.id} in changelog channel ignored (doesn't contain ```).")

# --- Control Functions ---
async def start_discord():
    """Start the Discord client."""
    try:
        logger.info("🔄 Starting Discord client...")
        await client.start(DISCORD_TOKEN)
    except discord.LoginFailure:
        logger.critical("❌ Discord Login Failed: Invalid token.")
        raise
    except Exception as e:
        logger.critical(f"❌ Unexpected error starting Discord client: {type(e).__name__} - {e}")
        raise

async def wait_until_ready():
    """Wait until the Discord client is ready."""
    await client.wait_until_ready()

def is_ready():
    """Check if the Discord client is ready."""
    return client.is_ready()

# Functions to safely access channels after on_ready
def get_changelog_channel():
    return changelog_channel

def get_exp_boost_channel():
    return exp_boost_channel 