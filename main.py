import argparse
from services.crawler import crawl, start_monitoring


def main():
    parser = argparse.ArgumentParser(description='Obsidian Vault Crawler')
    parser.add_argument('--crawl', action='store_true', help='Crawl the vault once and exit')
    parser.add_argument('--monitor', action='store_true', help='Monitor the vault for changes')
    
    args = parser.parse_args()
    
    if args.crawl:
        print("Starting one-time crawl...")
        processed = crawl()
        print(f"Crawl complete. Processed {processed} files.")
    elif args.monitor:
        print("Starting monitoring mode...")
        start_monitoring()
    else:
        print("Please specify either --crawl or --monitor")
        print("Usage:")
        print("  python -m main --crawl    # Run one-time crawl")
        print("  python -m main --monitor  # Start monitoring for changes")


if __name__ == "__main__":
    main()
