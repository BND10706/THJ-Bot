import aiohttp
import json
import logging
from datetime import datetime
from typing import Optional
import traceback

# Import specific config variables and logger
from config import WIKI_API_URL, WIKI_API_KEY, WIKI_PAGE_ID, WIKI_HEADER, logger

# --- Wiki Formatting Functions ---

def format_changelog_for_wiki(content: str, timestamp: datetime, author: str) -> str:
    """Format a single changelog entry for wiki presentation."""
    if not content or not isinstance(content, str):
        logger.error(f"Invalid content type passed to format_changelog_for_wiki: {type(content)}")
        return "" # Return empty string for invalid content

    # Remove Discord markdown code blocks and trim whitespace
    content = content.replace('```', '').strip()

    # Ensure content isn't empty after stripping ```
    if not content:
        logger.warning("Content became empty after removing code blocks.")
        return ""

    # Format the entry
    formatted_entry = f"# {timestamp.strftime('%B %d, %Y')}\n" # Date heading
    formatted_entry += f"## {author}\n\n" # Author sub-heading
    formatted_entry += f"{content}\n\n" # The actual content
    formatted_entry += "---" # Horizontal rule separator

    return formatted_entry

async def process_wiki_content(current_content: str, new_entry_formatted: str) -> str:
    """
    Combine existing wiki content with a new formatted changelog entry,
    ensuring the header is preserved and the new entry is at the top.
    """
    logger.debug("Processing wiki content...")
    # Ensure new entry is valid
    if not new_entry_formatted:
        logger.warning("process_wiki_content received an empty formatted new entry. Returning current content.")
        return current_content

    # Find the header and the content body
    header = WIKI_HEADER
    body = ""
    if WIKI_HEADER in current_content:
        # Split carefully to preserve initial spacing/newlines after the header
        parts = current_content.split(WIKI_HEADER, 1)
        if len(parts) == 2:
            body = parts[1].lstrip('\n') # Remove leading newlines from the existing body
        else: # Header found but no content after it?
            body = ""
        logger.debug(f"Found existing header. Body length: {len(body)}")
    else:
        logger.warning("Wiki header not found in current content. Prepending default header.")
        # Treat all current content as the body, but it might be unstructured
        body = current_content.strip() # Trim whitespace just in case

    # Combine: Header + New Entry + Existing Body
    # Ensure proper spacing: Header\n\nNew Entry\n\nExisting Body
    # The new_entry already ends with "---"
    full_content = f"{header}\n\n{new_entry_formatted}"

    if body:
        full_content += f"\n\n{body}" # Add two newlines before the old content

    # Clean up potential excessive newlines (more than 2 consecutive)
    while '\n\n\n' in full_content:
        full_content = full_content.replace('\n\n\n', '\n\n')

    logger.debug(f"Processed content length: {len(full_content)}")
    return full_content.strip() # Return stripped final content

# --- Wiki API Interaction ---

async def update_wiki_page(content: str, page_id: int) -> bool:
    """
    Update the specified wiki page with new content.
    Handles the update and render mutations.
    Returns True if successful, False otherwise.
    """
    if not all([WIKI_API_URL, WIKI_API_KEY]):
        logger.error("Wiki API URL or Key is not configured. Cannot update wiki.")
        return False
    if not page_id:
        logger.error("Wiki Page ID is not configured. Cannot update wiki.")
        return False
    if not content or not isinstance(content, str):
        logger.error("Invalid or empty content provided to update_wiki_page.")
        return False

    logger.info(f"Attempting to update Wiki page ID: {page_id}")
    headers = {
        'Authorization': f'Bearer {WIKI_API_KEY}',
        'Content-Type': 'application/json'
    }

    # Mutation to update content and ensure it's published
    update_mutation = """
    mutation UpdatePage($id: Int!, $content: String!) {
      pages {
        update(id: $id, content: $content, isPublished: true, description: "Automated changelog update") {
          responseResult {
            succeeded
            errorCode
            slug
            message
          }
        }
      }
    }
    """
    variables = {"id": page_id, "content": content}

    # Mutation to render the page after update
    render_mutation = """
    mutation RenderPage($id: Int!) {
      pages {
        render(id: $id) {
          responseResult {
            succeeded
            message
          }
        }
      }
    }
    """

    try:
        async with aiohttp.ClientSession() as session:
            # Step 1: Update Page Content
            logger.debug(f"Executing update mutation for page {page_id}...")
            async with session.post(WIKI_API_URL, json={"query": update_mutation, "variables": variables}, headers=headers) as response:
                response_status = response.status
                response_data = await response.json()
                logger.debug(f"Update mutation response status: {response_status}")
                logger.debug(f"Update mutation response data: {json.dumps(response_data)}")

                if response_status != 200 or 'errors' in response_data:
                    graphql_errors = response_data.get('errors', [])
                    error_msg = f"GraphQL errors during update: {[err.get('message') for err in graphql_errors]}" if graphql_errors else f"HTTP status {response_status}"
                    # Specific known ignorable error check
                    is_ignorable_map_error = any("Cannot read properties of undefined (reading 'map')" in err.get('message', '') for err in graphql_errors)

                    if is_ignorable_map_error:
                        logger.warning("Received known 'map' error during update, proceeding to render step...")
                        # We assume the update likely worked despite the error message from Wiki.js GQL response
                    else:
                        logger.error(f"Failed to update wiki page ({page_id}): {error_msg}")
                        return False
                else:
                    update_result = response_data.get('data', {}).get('pages', {}).get('update', {}).get('responseResult', {})
                    if not update_result.get('succeeded', False):
                         # Check again for the specific ignorable error in the success=false message
                        if "Cannot read properties of undefined (reading 'map')" in update_result.get('message', ''):
                            logger.warning("Received known 'map' error message in update result, proceeding to render step...")
                        else:
                            logger.error(f"Update mutation failed for page {page_id}: {update_result.get('message', 'Unknown error')}")
                            return False
                    else:
                        logger.info(f"Update mutation successful for page {page_id}.")

            # Step 2: Render Page (Attempt regardless of 'map' error in step 1)
            logger.debug(f"Executing render mutation for page {page_id}...")
            async with session.post(WIKI_API_URL, json={"query": render_mutation, "variables": {"id": page_id}}, headers=headers) as response:
                response_status = response.status
                response_data = await response.json()
                logger.debug(f"Render mutation response status: {response_status}")
                logger.debug(f"Render mutation response data: {json.dumps(response_data)}")

                if response_status != 200 or 'errors' in response_data:
                    graphql_errors = response_data.get('errors', [])
                    error_msg = f"GraphQL errors during render: {[err.get('message') for err in graphql_errors]}" if graphql_errors else f"HTTP status {response_status}"
                    logger.error(f"Failed to render wiki page ({page_id}): {error_msg}")
                    return False
                else:
                    render_result = response_data.get('data', {}).get('pages', {}).get('render', {}).get('responseResult', {})
                    if not render_result.get('succeeded', False):
                        logger.error(f"Render mutation failed for page {page_id}: {render_result.get('message', 'Unknown error')}")
                        return False
                    else:
                        logger.info(f"✅ Wiki page {page_id} updated and rendered successfully.")
                        return True

    except aiohttp.ClientError as e:
        logger.error(f"Network error updating wiki page {page_id}: {e}")
        return False
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON response from wiki API: {e}")
        # Log the raw response text if possible and safe
        try:
            raw_text = await response.text()
            logger.debug(f"Raw wiki response text: {raw_text[:500]}") # Log first 500 chars
        except Exception as read_err:
            logger.error(f"Could not read raw response text: {read_err}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error in update_wiki_page for page {page_id}: {type(e).__name__} - {e}")
        logger.debug(traceback.format_exc())
        return False

async def get_wiki_content(page_id: int) -> Optional[str]:
    """Fetches the current content of a specific wiki page."""
    if not all([WIKI_API_URL, WIKI_API_KEY]):
        logger.error("Wiki API URL or Key is not configured. Cannot get wiki content.")
        return None
    if not page_id:
        logger.error("Wiki Page ID is not configured. Cannot get wiki content.")
        return None

    logger.info(f"Fetching current Wiki content for page {page_id}...")
    headers = {
        'Authorization': f'Bearer {WIKI_API_KEY}',
        'Content-Type': 'application/json'
    }
    query = """
    query GetPageContent($id: Int!) {
      pages {
        single(id: $id) {
          content
        }
      }
    }
    """
    variables = {"id": page_id}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(WIKI_API_URL, json={"query": query, "variables": variables}, headers=headers) as response:
                response_status = response.status
                if response_status != 200:
                    logger.error(f"Failed to fetch wiki content (page {page_id}). Status: {response_status}")
                    return None

                response_data = await response.json()
                logger.debug(f"Get content response data: {json.dumps(response_data)}")

                if 'errors' in response_data:
                    graphql_errors = response_data.get('errors', [])
                    error_msg = f"GraphQL errors fetching content: {[err.get('message') for err in graphql_errors]}"
                    logger.error(error_msg)
                    return None

                page_data = response_data.get('data', {}).get('pages', {}).get('single')
                if page_data and 'content' in page_data:
                    logger.info(f"✓ Successfully retrieved current Wiki content (page {page_id})")
                    return page_data['content']
                else:
                    logger.warning(f"⚠️ No content found for wiki page {page_id} or unexpected response structure.")
                    return "" # Return empty string if page exists but has no content

    except aiohttp.ClientError as e:
        logger.error(f"Network error fetching wiki content (page {page_id}): {e}")
        return None
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON response from wiki API when fetching content: {e}")
        try:
            raw_text = await response.text()
            logger.debug(f"Raw wiki response text: {raw_text[:500]}")
        except Exception as read_err:
            logger.error(f"Could not read raw response text: {read_err}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error fetching wiki content (page {page_id}): {type(e).__name__} - {e}")
        logger.debug(traceback.format_exc())
        return None 