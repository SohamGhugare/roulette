from pathlib import Path
from typing import List, Set
import os

# Base configuration
class Config:
    # Default Obsidian vault path
    VAULT_PATH = os.path.expanduser("~/Documents/Obsidian Vault")
    
    # Output file for crawled content
    OUTPUT_FILE = "data.txt"
    
    # Directories to ignore (relative to VAULT_PATH)
    IGNORE_DIRS = [
        "Daily Notes",
        "Excalidraw"
    ]
    
    # File patterns/content to ignore
    IGNORE_PATTERNS = [
        "---\nexcalidraw-plugin: parsed\ntags: [excalidraw]\n---"
    ]
    
    # File extensions to process (only .md files for Obsidian)
    ALLOWED_EXTENSIONS = {'.md'}
    
    @classmethod
    def get_ignore_dirs(cls) -> List[str]:
        """Get full paths of directories to ignore"""
        return [str(Path(cls.VAULT_PATH) / d) for d in cls.IGNORE_DIRS]
    
    @classmethod
    def should_ignore_file(cls, file_path: str) -> bool:
        """Check if a file should be ignored based on its content"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                # Check first 10 lines for Excalidraw tag
                for _ in range(10):
                    line = f.readline()
                    if 'tags: [excalidraw]' in line:
                        return True
                    if not line:  # End of file
                        break
                
                # Check for other ignore patterns
                f.seek(0)
                content = f.read(200)
                return any(pattern in content for pattern in cls.IGNORE_PATTERNS)
        except Exception:
            return True  # Ignore files that can't be read
