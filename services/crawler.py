import os
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from typing import Set

from config import Config


class ObsidianCrawler(FileSystemEventHandler):
    def __init__(self, output_file: str):
        self.output_file = output_file
        self.processed_files: Set[str] = set()
        self.ignored_dirs = set(Config.get_ignore_dirs())

    def is_ignored(self, file_path: str) -> bool:
        """Check if a file should be ignored based on path or content"""
        # Skip directories in ignored list
        if any(file_path.startswith(ignored) for ignored in self.ignored_dirs):
            return True

        # Skip files with ignored extensions
        if Path(file_path).suffix.lower() not in Config.ALLOWED_EXTENSIONS:
            return True

        # Check file content for ignored patterns
        if Config.should_ignore_file(file_path):
            return True

        return False

    def initialize_output(self):
        """Initialize or clear the output file"""
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write("")

    def process_file(self, file_path: str) -> bool:
        """Process a single file and append its contents to the output"""
        if file_path in self.processed_files or self.is_ignored(file_path):
            return False

        try:
            # Get relative path for display
            rel_path = os.path.relpath(file_path, os.path.expanduser('~'))
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
            
            # Append to output file
            with open(self.output_file, 'a', encoding='utf-8') as out_f:
                out_f.write(f"\n\n{'='*80}\n")
                out_f.write(f"FILE: {rel_path}\n")
                out_f.write(f"{'='*80}\n\n")
                out_f.write(content)
                out_f.write("\n")
            
            self.processed_files.add(file_path)
            print(f"Processed: {rel_path}")
            return True
            
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")
            return False

    def on_created(self, event):
        if not event.is_directory:
            self.process_file(event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self.process_file(event.src_path)


def crawl() -> int:
    """Crawl the vault once and return number of files processed"""
    crawler = ObsidianCrawler(Config.OUTPUT_FILE)
    crawler.initialize_output()
    
    processed_count = 0
    
    for root, dirs, files in os.walk(Config.VAULT_PATH):
        # Skip ignored directories
        dirs[:] = [d for d in dirs if not any(
            str(Path(root) / d).startswith(ignored) 
            for ignored in crawler.ignored_dirs
        )]
        
        for file in files:
            file_path = os.path.join(root, file)
            if crawler.process_file(file_path):
                processed_count += 1
    
    return processed_count


def start_monitoring():
    """Start watching the vault for changes"""
    if not os.path.exists(Config.VAULT_PATH):
        print(f"Error: Vault directory not found at {Config.VAULT_PATH}")
        return

    # Initial crawl
    print("Performing initial crawl...")
    processed = crawl()
    print(f"Initial crawl complete. Processed {processed} files.")
    
    # Set up file watcher
    event_handler = ObsidianCrawler(Config.OUTPUT_FILE)
    observer = Observer()
    
    observer.schedule(
        event_handler,
        path=Config.VAULT_PATH,
        recursive=True
    )
    
    print(f"\nStarting to monitor {Config.VAULT_PATH}...")
    print(f"Output will be saved to {os.path.abspath(Config.OUTPUT_FILE)}")
    print("Press Ctrl+C to stop monitoring")
    
    try:
        observer.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nStopped monitoring")
    observer.join()