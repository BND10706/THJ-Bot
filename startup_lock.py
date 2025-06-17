import os
import time
import json
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class StartupLock:
    """Simple file-based lock for coordinating startup between services"""
    
    def __init__(self, lock_file="/app/data/.startup.lock"):
        self.lock_file = Path(lock_file)
        self.lock_timeout = 300  # 5 minutes
    
    def acquire(self, service_name):
        """Acquire the startup lock"""
        while True:
            try:
                # Check if lock exists and is stale
                if self.lock_file.exists():
                    with open(self.lock_file, 'r') as f:
                        lock_data = json.load(f)
                    
                    # Check if lock is stale
                    if time.time() - lock_data['timestamp'] > self.lock_timeout:
                        logger.warning(f"Removing stale lock from {lock_data['service']}")
                        self.lock_file.unlink()
                    else:
                        # Lock is held, wait
                        time.sleep(1)
                        continue
                
                # Try to create lock
                lock_data = {
                    'service': service_name,
                    'timestamp': time.time(),
                    'pid': os.getpid()
                }
                
                # Use exclusive create to prevent race
                fd = os.open(str(self.lock_file), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                with os.fdopen(fd, 'w') as f:
                    json.dump(lock_data, f)
                
                return True
                
            except FileExistsError:
                # Another service got the lock
                time.sleep(1)
                continue
            except Exception as e:
                logger.error(f"Error acquiring lock: {e}")
                time.sleep(1)
    
    def release(self):
        """Release the startup lock"""
        try:
            if self.lock_file.exists():
                self.lock_file.unlink()
        except Exception as e:
            logger.error(f"Error releasing lock: {e}")