import os
import logging
import sys
from dotenv import load_dotenv

# --- Logging Setup ---

# Configure logging for Azure compatibility and general use
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout) # Ensure logs go to stdout
    ]
)

# Get the root logger
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

# Remove any existing handlers (to avoid duplicates if re-run)
for handler in root_logger.handlers[:]:
    root_logger.removeHandler(handler)

# Add stdout handler back to the root logger
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
root_logger.addHandler(stdout_handler)

# Get a logger instance for this module
logger = logging.getLogger(__name__)

# --- Environment Variable Loading ---

logger.info("Loading environment variables...")
load_dotenv()

# --- Core Bot Configuration ---
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
CHANGELOG_CHANNEL_ID = os.getenv('CHANGELOG_CHANNEL_ID')
EXP_BOOST_CHANNEL_ID = os.getenv('EXP_BOOST_CHANNEL_ID')
PATCHER_TOKEN = os.getenv('PATCHER_TOKEN')

# --- Wiki Configuration ---
WIKI_API_URL = os.getenv('WIKI_API_URL')
WIKI_API_KEY = os.getenv('WIKI_API_KEY')
WIKI_PAGE_ID = os.getenv('WIKI_PAGE_ID')

# --- Server Configuration ---
PORT = int(os.getenv('PORT', '80')) # Default to 80 if not set

# --- Type Conversions and Validations ---

try:
    if CHANGELOG_CHANNEL_ID:
        CHANGELOG_CHANNEL_ID = int(CHANGELOG_CHANNEL_ID)
    else:
        logger.warning("CHANGELOG_CHANNEL_ID is not set.")
except ValueError:
    logger.error("Invalid CHANGELOG_CHANNEL_ID provided. Must be an integer.")
    raise ValueError("Invalid CHANGELOG_CHANNEL_ID")

try:
    if EXP_BOOST_CHANNEL_ID:
        EXP_BOOST_CHANNEL_ID = int(EXP_BOOST_CHANNEL_ID)
    else:
        logger.warning("EXP_BOOST_CHANNEL_ID not set - exp boost functionality will be disabled")
except ValueError:
    logger.error("Invalid EXP_BOOST_CHANNEL_ID provided. Must be an integer.")
    EXP_BOOST_CHANNEL_ID = None # Disable if invalid

try:
    if WIKI_PAGE_ID:
        WIKI_PAGE_ID = int(WIKI_PAGE_ID)
    else:
        logger.warning("WIKI_PAGE_ID not set - wiki integration may be limited")
except ValueError:
    logger.error("Invalid WIKI_PAGE_ID provided. Must be an integer.")
    WIKI_PAGE_ID = None # Disable if invalid


# --- Constants ---
VALUE_CHANNEL_ID = 1319011465960882197 # Consider moving to env vars if it changes
WIKI_HEADER = """![change-logs.webp](/change-logs.webp){.align-center}
# THJ Change-Logs
(Newest is up top, Oldest is at the bottom.)"""

# --- Helper Functions ---
def mask_sensitive_string(s: str) -> str:
    """Mask sensitive string by showing only first and last 4 characters"""
    if not s:
        return ""
    if len(s) <= 8:
        return "*" * len(s)
    return f"{s[:4]}...{s[-4:]}"

# --- Environment Variable Check ---
def check_environment_variables():
    """Checks and logs the status of required and optional environment variables."""
    logger.info("=== Environment Check ===")
    required_vars = {
        'DISCORD_TOKEN': DISCORD_TOKEN,
        'CHANGELOG_CHANNEL_ID': CHANGELOG_CHANNEL_ID,
        'PATCHER_TOKEN': PATCHER_TOKEN
    }
    missing_required = False
    for var_name, var_value in required_vars.items():
        if not var_value:
            logger.error(f"❌ Required environment variable {var_name} is missing!")
            missing_required = True
        else:
            # Mask sensitive tokens in logs
            display_value = mask_sensitive_string(str(var_value)) if 'TOKEN' in var_name or 'KEY' in var_name else var_value
            logger.info(f"✓ {var_name}: {display_value}")

    if missing_required:
        raise ValueError("Missing one or more required environment variables. Check logs.")

    logger.info("\n--- Optional Variables ---")
    optional_vars = {
        'EXP_BOOST_CHANNEL_ID': EXP_BOOST_CHANNEL_ID,
        'WIKI_API_URL': WIKI_API_URL,
        'WIKI_API_KEY': WIKI_API_KEY,
        'WIKI_PAGE_ID': WIKI_PAGE_ID,
        'PORT': PORT
    }
    for var_name, var_value in optional_vars.items():
        status = "✓ configured" if var_value else "⚪ not set (optional)"
        # Mask sensitive tokens in logs
        display_value = mask_sensitive_string(str(var_value)) if 'TOKEN' in var_name or 'KEY' in var_name else var_value
        logger.info(f"{var_name}: {status} ({display_value if var_value else 'N/A'})")

    logger.info("=== Environment Check Complete ===")

# Run the check function when the module is loaded
check_environment_variables() 