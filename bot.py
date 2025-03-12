import os
import discord
from fastapi import FastAPI, HTTPException, Security, Depends
from dotenv import load_dotenv
from datetime import datetime
import asyncio
import uvicorn
from typing import Optional
import aiohttp
from fastapi.security import APIKeyHeader
import json
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANGELOG_CHANNEL_ID = int(os.getenv('CHANGELOG_CHANNEL_ID')) 
PATCHER_TOKEN = os.getenv('PATCHER_TOKEN')

# File to store the last processed message ID
LAST_MESSAGE_FILE = "last_message.json"

# Load last processed message ID from file
def load_last_message_id():
    try:
        if os.path.exists(LAST_MESSAGE_FILE):
            with open(LAST_MESSAGE_FILE, 'r') as f:
                data = json.load(f)
                return int(data.get('last_message_id', 0))
    except Exception as e:
        print(f"Error loading last message ID: {str(e)}")
    return 0

# Save last processed message ID to file
def save_last_message_id(message_id):
    try:
        with open(LAST_MESSAGE_FILE, 'w') as f:
            json.dump({'last_message_id': str(message_id)}, f)
    except Exception as e:
        print(f"Error saving last message ID: {str(e)}")

# Initialize last_processed_message_id from file
last_processed_message_id = load_last_message_id()
print(f"\n📝 Last processed message ID: {last_processed_message_id}")

# Ensure we use the port provided by Azure
PORT = int(os.getenv('PORT', '80'))
print(f"\n🔧 Configured to use port: {PORT}")

# Wiki variables
WIKI_API_URL = os.getenv('WIKI_API_URL')
WIKI_API_KEY = os.getenv('WIKI_API_KEY')
WIKI_PAGE_ID = os.getenv('WIKI_PAGE_ID') 

def mask_sensitive_string(s: str) -> str:
    """Mask sensitive string by showing only first and last 4 characters"""
    if not s:
        return ""
    if len(s) <= 8:
        return "*" * len(s)
    return f"{s[:4]}...{s[-4:]}"

# Verify required environment variables
print("\n=== Environment Check ===")
required_vars = {
    'DISCORD_TOKEN': TOKEN,
    'CHANGELOG_CHANNEL_ID': CHANGELOG_CHANNEL_ID,
    'PATCHER_TOKEN': PATCHER_TOKEN
}

for var_name, var_value in required_vars.items():
    if not var_value:
        print(f"❌ {var_name} is missing!")
        raise ValueError(f"{var_name} environment variable is required")
    else:
        print(f"✓ {var_name} configured")

# Log Wiki variables status
print("\n=== Optional Wiki Variables ===")
wiki_vars = {
    'WIKI_API_URL': WIKI_API_URL,
    'WIKI_API_KEY': WIKI_API_KEY,
    'WIKI_PAGE_ID': WIKI_PAGE_ID
}

for var_name, var_value in wiki_vars.items():
    status = "✓ configured" if var_value else "⚪ not set (optional)"
    print(f"{var_name}: {status}")

print("=== Environment Check Complete ===\n")

# Set up Discord client
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
client = discord.Client(intents=intents)

# Set up FastAPI
app = FastAPI()

# Set up security
api_key_header = APIKeyHeader(name="X-Patcher-Token", auto_error=True)

async def verify_token(api_key: str = Security(api_key_header)):
    if api_key != PATCHER_TOKEN:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication token"
        )
    return api_key

def format_changelog_for_wiki(content, timestamp, author):
    """Format changelog content for wiki presentation with standardized header"""
    formatted = f"# {timestamp.strftime('%B %d, %Y')}\n"
    formatted += f"## {author}\n\n"
    
    content = content.replace('```', '').strip()
    
    formatted += f"{content}\n\n---\n\n"
    return formatted

async def get_date_range():
    """Get the date range for the changelog header"""
    try:
        # Get the earliest and latest messages
        messages = []
        async for message in changelog_channel.history(limit=None, oldest_first=True):
            messages.append(message)
            
        if not messages:
            return "(No changelogs available)"
            
        earliest = messages[0].created_at
        latest = messages[-1].created_at
        
        # Add one year to the latest date for the range
        latest_plus_year = latest.replace(year=latest.year + 1)
        
        return f"({earliest.strftime('%b %d, %Y')} – {latest_plus_year.strftime('%b %d, %Y')})"
    except Exception as e:
        print(f"Error getting date range: {str(e)}")
        return "(Date range unavailable)"

changelog_channel = None

@client.event
async def on_message(message):
    """Handle new messages in Discord"""
    if message.channel.id == CHANGELOG_CHANNEL_ID:
        print(f"\n🔔 New changelog entry from: {message.author.display_name}")

@client.event
async def on_ready():
    global changelog_channel
    print(f'\n🤖 Bot connected successfully!')
    
    for guild in client.guilds:
        for channel in guild.channels:
            if channel.id == CHANGELOG_CHANNEL_ID:
                changelog_channel = channel
                print(f'✅ Found changelog channel')
                return
    
    if not changelog_channel:
        print(f'❌ Could not find changelog channel')

@app.get("/changelog", dependencies=[Depends(verify_token)])
async def get_changelog(count: Optional[int] = 1, all: Optional[bool] = False):
    """
    Get the latest changelog(s) from Discord
    Requires X-Patcher-Token header for authentication.
    Optional parameters:
    - count: number of changelogs to retrieve (default: 1)
    - all: if True, retrieves all messages ever posted (ignores count parameter)
    Example: /changelog?count=3
    Example: /changelog?all=true
    """
    if not changelog_channel:
        print(f'Channel not found. Looking for ID: {CHANGELOG_CHANNEL_ID}')
        raise HTTPException(status_code=500, detail=f"Discord bot not ready or channel {CHANGELOG_CHANNEL_ID} not found")
    
    try:
        if all:
            print(f'Attempting to fetch ALL messages from channel {changelog_channel.name}')
            messages = [message async for message in changelog_channel.history(limit=None, oldest_first=False)]
        else:
            print(f'Attempting to fetch {count} message(s) from channel {changelog_channel.name}')
            messages = [message async for message in changelog_channel.history(limit=count)]

        if not messages:
            print('No messages found in channel')
            return {
                "total": 0,
                "changelogs": []
            }

        changelogs = []
        for message in messages:
            formatted_content = format_changelog_for_wiki(
                message.content, 
                message.created_at,
                message.author.display_name
            )
            changelogs.append({
                "raw_content": message.content,
                "formatted_content": formatted_content,
                "author": message.author.display_name,
                "timestamp": message.created_at.isoformat(),
                "message_id": str(message.id)
            })
            
        print(f'Successfully fetched {len(changelogs)} changelog(s)')
        return {
            "total": len(changelogs),
            "changelogs": sorted(changelogs, key=lambda x: x["timestamp"], reverse=True)
        }
    except Exception as e:
        print(f'Error fetching changelogs: {str(e)}')
        raise HTTPException(status_code=500, detail=str(e))

async def update_wiki_page(content, page_id):
    """Update Wiki.js page with GraphQL"""
    try:
        print(f"\n=== Attempting to update Wiki page {page_id} ===")
        headers = {
            'Authorization': f'Bearer {WIKI_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        # Add the header with image and date range
        if not content.startswith("![change-logs.webp"):
            date_range = await get_date_range()
            header = f"![change-logs.webp](/change-logs.webp){{.align-center}}\n# THJ Change-Logs\n{date_range}\n\n"
            content = header + content.replace("# Changelog\n\n", "")
        
        escaped_content = content.replace('\\', '\\\\').replace('"', '\\"')
        
        update_mutation = {
            "query": """
            mutation ($id: Int!, $content: String!) {
              pages {
                update(
                  id: $id
                  content: $content
                  editor: "markdown"
                  description: "Updated by Changelog Bot"
                  isPublished: true
                  isPrivate: false
                  locale: "en"
                  tags: ["changelog"]
                  title: "Changelog"
                ) {
                  responseResult {
                    succeeded
                    slug
                    message
                  }
                  page {
                    id
                    path
                  }
                }
              }
            }
            """,
            "variables": {
                "id": page_id,
                "content": escaped_content
            }
        }
        
        print("Sending update request to Wiki.js...")
        print(f"Page ID: {page_id}")
        print("Content length: {} characters".format(len(content)))
        
        async with aiohttp.ClientSession() as session:
            async with session.post(
                WIKI_API_URL,
                json=update_mutation,
                headers=headers
            ) as update_response:
                update_data = await update_response.json()
                print(f"Response status: {update_response.status}")
                
                if 'errors' in update_data:
                    print("❌ GraphQL errors occurred:")
                    for error in update_data['errors']:
                        print(f"Error message: {error.get('message', 'No message')}")
                        print(f"Error details: {error}")
                    return False
                    
                if 'data' in update_data:
                    result = update_data['data']['pages']['update']['responseResult']
                    if result['succeeded']:
                        print(f"✅ Successfully updated Wiki page {page_id}")
                        if 'page' in update_data['data']['pages']['update']:
                            page = update_data['data']['pages']['update']['page']
                            print(f"Updated page path: {page.get('path', 'unknown')}")
                        return True
                    else:
                        print(f"❌ Update failed: {result.get('message', 'No error message provided')}")
                        return False
                        
                print("❌ Unexpected response format")
                print(f"Full response: {update_data}")
                return False
                    
    except Exception as e:
        print(f"❌ Error updating Wiki page: {type(e).__name__}")
        print(f"Error details: {str(e)}")
        return False

@app.post("/test-wiki", dependencies=[Depends(verify_token)])
async def test_wiki_update():
    """
    Test endpoint to verify Wiki.js API connection
    Requires X-Patcher-Token header for authentication.
    """
    page_id = 114
    print(f"Testing access for page ID: {page_id}")
    
    test_content = """
# Test Changelog

Fri Mar 15 2024 - Posted by: Bot

- This is a test changelog entry
- Testing Wiki.js REST API connection
- Please verify this appears on the wiki
    """
    
    success = await update_wiki_page(test_content, page_id)
    if success:
        return {"status": "success", "message": "Wiki updated successfully", "page_id": page_id}
    else:
        raise HTTPException(status_code=500, detail="Failed to update wiki")

async def get_page_id(path):
    """Get Wiki.js page ID from path"""
    try:
        headers = {
            'Authorization': f'Bearer {WIKI_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        # GraphQL query to get page ID
        query = """
        query GetPage($path: String!) {
          pages {
            single(path: $path) {
              id
            }
          }
        }
        """
        
        variables = {
            "path": path
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(
                WIKI_API_URL,
                json={
                    "query": query,
                    "variables": variables
                },
                headers=headers
            ) as response:
                response_data = await response.json()
                print(f"Page lookup response: {response_data}")
                if response.status == 200 and response_data.get('data'):
                    page_data = response_data['data']['pages']['single']
                    if page_data:
                        return page_data['id']
                return None
    except Exception as e:
        print(f"Error looking up page: {str(e)}")
        return None

@app.get("/lookup-page/{path:path}", dependencies=[Depends(verify_token)])
async def lookup_page(path: str):
    """
    Look up a Wiki.js page ID by path
    Requires X-Patcher-Token header for authentication.
    """
    page_id = await get_page_id(path)
    if page_id:
        return {"page_id": page_id, "path": path}
    else:
        raise HTTPException(status_code=404, detail=f"Page not found: {path}")

async def list_pages():
    """List all Wiki.js pages"""
    try:
        headers = {
            'Authorization': f'Bearer {WIKI_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        query = """
        query ListPages {
          pages {
            list {
              id
              path
              title
            }
          }
        }
        """
        
        async with aiohttp.ClientSession() as session:
            async with session.post(
                WIKI_API_URL,
                json={
                    "query": query
                },
                headers=headers
            ) as response:
                response_data = await response.json()
                print(f"Pages list response: {response_data}")
                if response.status == 200 and response_data.get('data'):
                    return response_data['data']['pages']['list']
                return None
    except Exception as e:
        print(f"Error listing pages: {str(e)}")
        return None

@app.get("/list-pages", dependencies=[Depends(verify_token)])
async def get_pages():
    """
    List all Wiki.js pages to help find the correct path
    Requires X-Patcher-Token header for authentication.
    """
    pages = await list_pages()
    if pages:
        return {"pages": pages}
    else:
        raise HTTPException(status_code=500, detail="Failed to list pages")

@app.get("/test-wiki-read", dependencies=[Depends(verify_token)])
async def test_wiki_read():
    """
    Test endpoint to verify Wiki.js API read access
    Requires X-Patcher-Token header for authentication.
    """
    page_id = 114  # Using known page ID
    print(f"Testing read access for page ID: {page_id}")
    
    try:
        headers = {
            'Authorization': f'Bearer {WIKI_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        query = """
        query {
          pages {
            single(id: %d) {
              id
              path
              title
              content
              isPublished
              isPrivate
              createdAt
              updatedAt
            }
          }
        }
        """ % page_id
        
        async with aiohttp.ClientSession() as session:
            async with session.post(
                WIKI_API_URL,
                json={"query": query},
                headers=headers
            ) as response:
                response_data = await response.json()
                print(f"Read response: {response_data}")
                if 'errors' in response_data:
                    print(f"Failed to read page: {response_data['errors']}")
                    raise HTTPException(status_code=500, detail="Failed to read wiki page")
                return response_data['data']['pages']['single']
                    
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print(f"Full error details: {repr(e)}")
        raise HTTPException(status_code=500, detail=str(e))

async def check_and_update_wiki():
    """Periodically check Discord channel for new messages and update Wiki"""
    global last_processed_message_id
    
    while True:
        try:
            if changelog_channel:
                logger.info(f"\n=== Checking for new messages at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")
                messages_found = False
                
                # Only get the most recent message
                async for message in changelog_channel.history(limit=1):
                    messages_found = True
                    
                    if last_processed_message_id and message.id <= last_processed_message_id:
                        logger.info(f"No new messages to process (Last ID: {last_processed_message_id})")
                        break
                        
                    logger.info(f"New message found from: {message.author.display_name}")
                    
                    # Get current content first
                    page_id = int(os.getenv('WIKI_PAGE_ID'))
                    try:
                        headers = {
                            'Authorization': f'Bearer {WIKI_API_KEY}',
                            'Content-Type': 'application/json'
                        }
                        query = """
                        query {
                          pages {
                            single(id: %d) {
                              content
                            }
                          }
                        }
                        """ % page_id
                        
                        logger.info(f"Fetching current Wiki content for page {page_id}...")
                        async with aiohttp.ClientSession() as session:
                            async with session.post(
                                WIKI_API_URL,
                                json={"query": query},
                                headers=headers
                            ) as response:
                                response_data = await response.json()
                                if 'data' in response_data and response_data['data']['pages']['single']:
                                    current_content = response_data['data']['pages']['single']['content']
                                    # Split content to preserve header
                                    if "![change-logs.webp" in current_content:
                                        header_parts = current_content.split("\n\n", 3)
                                        header = "\n\n".join(header_parts[:3])  # Preserve image, title, and date range
                                        existing_content = header_parts[3] if len(header_parts) > 3 else ""
                                    else:
                                        header = ""
                                        existing_content = current_content
                                    logger.info("✓ Successfully retrieved current Wiki content")
                                else:
                                    header = ""
                                    existing_content = ""
                                    logger.warning("⚠️ No existing content found")
                    
                    except Exception as e:
                        logger.error(f"❌ Error getting current content: {type(e).__name__}")
                        logger.error(f"Error details: {str(e)}")
                        header = ""
                        existing_content = ""
                    
                    new_entry = format_changelog_for_wiki(
                        message.content,
                        message.created_at,
                        message.author.display_name
                    )
                    
                    # If no header exists, create one
                    if not header:
                        date_range = await get_date_range()
                        header = f"![change-logs.webp](/change-logs.webp){{.align-center}}\n# THJ Change-Logs\n{date_range}"
                    
                    # Combine header, new entry, and existing content
                    full_content = f"{header}\n\n{new_entry}{existing_content.strip()}"
                    full_content = full_content.replace('\n\n\n', '\n\n')
                    logger.info("Content prepared for update")
                    
                    success = await update_wiki_page(full_content, page_id)
                    if success:
                        logger.info("✅ Successfully updated Wiki with new changelog")
                        last_processed_message_id = message.id
                        save_last_message_id(message.id)  # Save the ID after successful update
                    else:
                        logger.error("❌ Failed to update Wiki")
                
                if not messages_found:
                    logger.info("No new messages found in channel")
                        
            else:
                logger.warning("⏳ Waiting for changelog channel to be ready...")
                
        except Exception as e:
            logger.error(f"❌ Error in check_and_update_wiki: {type(e).__name__}")
            logger.error(f"Error details: {str(e)}")
            
        logger.info("\nWaiting 30 seconds before next check...")
        await asyncio.sleep(30)  # Check every 30 seconds

async def start_discord():
    """Start the Discord client"""
    try:
        print("\n🔄 Starting Discord client...")
        await client.start(TOKEN)
    except discord.LoginFailure:
        print("\n❌ Failed to log in to Discord!")
        raise
    except Exception as e:
        print(f"\n❌ Connection error: {type(e).__name__}")
        raise

async def start_api():
    """Start the FastAPI server"""
    try:
        print(f"\n🚀 Starting FastAPI server on port {PORT}...")
        print(f"Host: 0.0.0.0")
        print(f"Port: {PORT}")
        
        config = uvicorn.Config(app, host="0.0.0.0", port=PORT, log_level="info")
        server = uvicorn.Server(config)
        await server.serve()
    except Exception as e:
        print(f"❌ Failed to start FastAPI server: {str(e)}")
        print(f"Port attempted: {PORT}")
        print(f"Error type: {type(e).__name__}")
        raise

@app.get("/last-message", dependencies=[Depends(verify_token)])
async def get_last_message():
    """
    Get the last message from the changelog channel
    Requires X-Patcher-Token header for authentication.
    """
    try:
        print("\n=== Attempting to read last message ===")
        print(f"Channel ID we're looking for: {CHANGELOG_CHANNEL_ID}")
        
        if not client.is_ready():
            print("Discord client is not ready")
            return {"status": "error", "message": "Discord client is not ready"}
            
        if not changelog_channel:
            print("Changelog channel not found")
            return {"status": "error", "message": "Changelog channel not found"}
            
        print(f"Found channel: {changelog_channel.name}")
        
        # Get the last message
        messages = [message async for message in changelog_channel.history(limit=1)]
        
        if not messages:
            print("No messages found")
            return {"status": "success", "message": "No messages found"}
            
        last_message = messages[0]
        print(f"Found message: {last_message.content[:100]}...")
        
        return {
            "status": "success",
            "message": {
                "content": last_message.content,
                "author": last_message.author.display_name,
                "created_at": last_message.created_at.isoformat(),
                "id": last_message.id
            }
        }
        
    except Exception as e:
        print(f"Error reading last message: {str(e)}")
        print(f"Full error details: {repr(e)}")
        return {"status": "error", "message": str(e)}

@app.get("/patcher/latest", dependencies=[Depends(verify_token)])
async def get_latest_for_patcher():
    """
    Secure endpoint for the patcher to get the latest changelog entry.
    Requires X-Patcher-Token header for authentication.
    Returns the latest changelog message in a formatted structure.
    """
    try:
        print("\n=== Patcher requesting latest changelog ===")
        
        if not client.is_ready():
            raise HTTPException(status_code=503, detail="Discord client is not ready")
            
        if not changelog_channel:
            raise HTTPException(status_code=503, detail="Changelog channel not found")
            
        messages = [message async for message in changelog_channel.history(limit=1)]
        
        if not messages:
            return {
                "status": "success",
                "found": False,
                "message": "No changelog entries found"
            }
            
        last_message = messages[0]
        
        
        formatted_content = format_changelog_for_wiki(
            last_message.content,
            last_message.created_at,
            last_message.author.display_name
        )
        
        return {
            "status": "success",
            "found": True,
            "changelog": {
                "raw_content": last_message.content,
                "formatted_content": formatted_content,
                "author": last_message.author.display_name,
                "timestamp": last_message.created_at.isoformat(),
                "message_id": str(last_message.id)
            }
        }
        
    except Exception as e:
        print(f"Error in patcher endpoint: {str(e)}")
        print(f"Full error details: {repr(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/wiki/update-changelog", dependencies=[Depends(verify_token)])
async def update_wiki_with_all_changelogs():
    """
    Fetch all changelogs and update the wiki page with them.
    Requires X-Patcher-Token header for authentication.
    """
    print("\n=== Starting Wiki Changelog Update ===")
    
    # Check if wiki integration is configured
    if not all([WIKI_API_URL, WIKI_API_KEY, WIKI_PAGE_ID]):
        raise HTTPException(
            status_code=500,
            detail="Wiki integration is not fully configured. Please set WIKI_API_URL, WIKI_API_KEY, and WIKI_PAGE_ID."
        )
    
    try:
        # Get all changelogs using existing endpoint logic
        changelogs = await get_changelog(all=True)
        
        if not changelogs["total"]:
            return {
                "status": "success",
                "message": "No changelogs found to update"
            }
        
        # Format all changelogs for wiki
        formatted_content = "# Changelog\n\n"
        for changelog in changelogs["changelogs"]:
            formatted_content += changelog["formatted_content"]
        
        # Update the wiki page
        page_id = int(WIKI_PAGE_ID)
        success = await update_wiki_page(formatted_content, page_id)
        
        if success:
            return {
                "status": "success",
                "message": f"Successfully updated wiki with {changelogs['total']} changelog entries",
                "total_entries": changelogs["total"]
            }
        else:
            raise HTTPException(
                status_code=500,
                detail="Failed to update wiki page"
            )
            
    except Exception as e:
        print(f"❌ Error updating wiki with changelogs: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

async def main():
    """Run both Discord client and FastAPI server"""
    try:
        print("\n=== Starting Application ===")
        print(f"PORT: {PORT}")
        print(f"CHANGELOG_CHANNEL_ID: {CHANGELOG_CHANNEL_ID}")
        print("Starting Discord client...")
        
        # Start Discord client
        discord_task = asyncio.create_task(start_discord())
        
        # Wait for Discord to be ready
        timeout = 30  # 30 seconds timeout
        start_time = asyncio.get_event_loop().time()
        while not client.is_ready():
            if asyncio.get_event_loop().time() - start_time > timeout:
                raise TimeoutError("Discord client failed to connect within timeout period")
            print("⏳ Waiting for Discord client to be ready...")
            await asyncio.sleep(1)
        
        print("✅ Discord client is ready!")
        print("🔍 Looking for changelog channel...")
        
        if changelog_channel:
            print(f"✅ Found changelog channel: {changelog_channel.name}")
        else:
            print("❌ Could not find changelog channel!")
            raise ValueError("Changelog channel not found")
        
        # Start the wiki checker task
        wiki_task = asyncio.create_task(check_and_update_wiki())
        print("✅ Started wiki update checker (30-second intervals)")
        
        # Start FastAPI server
        print("\n=== Starting FastAPI Server ===")
        api_task = asyncio.create_task(start_api())
        
        # Wait for all tasks
        await asyncio.gather(discord_task, api_task, wiki_task)
        
    except TimeoutError as e:
        print(f"\n❌ Timeout error: {str(e)}")
        raise
    except ValueError as e:
        print(f"\n❌ Configuration error: {str(e)}")
        raise
    except Exception as e:
        print(f"\n❌ Error in main: {type(e).__name__}")
        print(f"Error details: {str(e)}")
        raise

if __name__ == "__main__":
    asyncio.run(main()) 