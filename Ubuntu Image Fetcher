import requests
import os
from urllib.parse import urlparse
import sys

# Define constants for file management and safety
MAX_FILE_SIZE_MB = 10
SUPPORTED_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif']
USER_AGENT = "Ubuntu Image Fetcher/1.0 (Python requests library)"

def fetch_and_save_image(url, fetched_urls):
    """
    Fetches and saves an image from a URL, with safety and deduplication checks.

    Args:
        url (str): The URL of the image to fetch.
        fetched_urls (set): A set of URLs that have already been processed
                           to prevent duplicate downloads.
    """
    # 1. Deduplication Check
    if url in fetched_urls:
        print(f"✓ Skipping URL: {url} - Already fetched.")
        return

    try:
        # 2. Add HTTP headers for responsible fetching
        headers = {'User-Agent': USER_AGENT}
        
        # 3. Check important HTTP headers before downloading the content
        # Use a HEAD request to get headers without downloading the full content
        response = requests.head(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Check content type and length
        content_type = response.headers.get('Content-Type', '')
        content_length_bytes = int(response.headers.get('Content-Length', 0))
        
        # Get filename and extension
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if '.' not in filename: # If no extension in filename
             filename = f"downloaded_image_{len(fetched_urls)}.jpeg"
        
        # 4. Implement precautions for unknown sources
        # Check if the content is actually an image and within size limits
        if not any(ext in content_type for ext in SUPPORTED_EXTENSIONS):
            print(f"✗ Error: URL {url} is not a supported image type ({content_type}).")
            return
        
        if content_length_bytes > MAX_FILE_SIZE_MB * 1024 * 1024:
            print(f"✗ Error: File size exceeds the {MAX_FILE_SIZE_MB}MB limit.")
            return

        # 5. Fetch the image content now that pre-checks have passed
        print(f"Fetching {url}...")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)
        
        filepath = os.path.join("Fetched_Images", filename)
        
        # Use a more robust check to avoid file name collisions
        # In a more advanced version, you might check a hash of the content
        # instead of just the filename to catch images with different names.
        if os.path.exists(filepath):
            print(f"✓ Skipping file: {filename} - A file with this name already exists.")
            fetched_urls.add(url) # Add to set to prevent re-checking
            return

        with open(filepath, 'wb') as f:
            f.write(response.content)
            
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        fetched_urls.add(url)
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ An unexpected error occurred for {url}: {e}")

def main():
    """
    Main function to run the Ubuntu Image Fetcher.
    Prompts the user for multiple URLs and processes them.
    """
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    print("Enter image URLs one by one. Type 'done' to finish.\n")
    
    urls_to_fetch = []
    while True:
        url = input("Please enter an image URL: ")
        if url.lower() == 'done':
            break
        urls_to_fetch.append(url)
        
    if not urls_to_fetch:
        print("No URLs entered. Exiting.")
        sys.exit()

    # Use a set to track fetched URLs for efficient lookups
    fetched_urls = set()
    
    for url in urls_to_fetch:
        fetch_and_save_image(url, fetched_urls)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
