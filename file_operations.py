import os
import json
import time
import tempfile
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class SafeFileOperations:
    """Thread-safe file operations using atomic writes"""
    
    @staticmethod
    def atomic_write(filepath, content, mode='w'):
        """
        Atomically write to a file by writing to temp file then renaming.
        This prevents partial reads and corrupted writes.
        """
        filepath = Path(filepath)
        
        # Create temp file in same directory (for atomic rename)
        temp_fd, temp_path = tempfile.mkstemp(
            dir=filepath.parent, 
            prefix=f".{filepath.name}.",
            suffix=".tmp"
        )
        
        try:
            # Write to temp file
            with os.fdopen(temp_fd, mode) as temp_file:
                temp_file.write(content)
                temp_file.flush()
                os.fsync(temp_file.fileno())  # Force write to disk
            
            # Atomic rename (on POSIX systems, this is atomic)
            os.replace(temp_path, filepath)
            
        except Exception as e:
            # Clean up temp file on error
            try:
                os.unlink(temp_path)
            except:
                pass
            raise e
    
    @staticmethod
    def safe_read(filepath, max_retries=3, retry_delay=0.1):
        """
        Safely read a file with retry logic for handling concurrent access.
        """
        filepath = Path(filepath)
        
        for attempt in range(max_retries):
            try:
                # Check if file exists
                if not filepath.exists():
                    return None
                
                # Read file
                with open(filepath, 'r') as f:
                    content = f.read()
                
                # Verify we got complete content (basic check)
                if content and not content.strip().endswith(('---', '}')):
                    # For markdown files, check if it looks complete
                    if filepath.suffix == '.md' and '## Entry' in content:
                        # Make sure we have a complete entry
                        if content.count('## Entry') != content.count('---\n\n'):
                            raise ValueError("Incomplete markdown file detected")
                
                return content
                
            except (IOError, OSError, ValueError) as e:
                if attempt < max_retries - 1:
                    logger.warning(f"Read attempt {attempt + 1} failed: {e}, retrying...")
                    time.sleep(retry_delay)
                else:
                    raise
    
    @staticmethod
    def append_safe(filepath, content):
        """
        Safely append to a file using read-modify-write with atomic write.
        """
        filepath = Path(filepath)
        
        # Read existing content
        existing = SafeFileOperations.safe_read(filepath) or ""
        
        # Append new content
        new_content = existing + content
        
        # Write atomically
        SafeFileOperations.atomic_write(filepath, new_content)