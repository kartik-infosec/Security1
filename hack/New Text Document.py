import requests
from requests.exceptions import RequestException, SSLError
import time

# Set proxy details
PROXY = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
}

# Disable SSL certificate validation for Burp Suite interception (if needed)
VERIFY_SSL = False

def fetch_urls_from_file(file_path):
    """Read URLs from the provided text file."""
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def send_request(url):
    """Send HTTP request to the URL and follow redirections."""
    try:
        # Append '/hello12345' to the URL
        modified_url = f"https://{url}/hello12345"
        print(f"Sending request to: {modified_url}")

        # Send the GET request with the proxy and SSL verification disabled if necessary
        response = requests.get(modified_url, proxies=PROXY, verify=VERIFY_SSL, allow_redirects=True)

        # Handle successful response
        if response.status_code == 200:
            print(f"Request successful: {modified_url}")
            print(f"Response status code: {response.status_code}")
            print(f"Final URL after redirection: {response.url}")
        else:
            print(f"Request failed with status code: {response.status_code}")
    
    except SSLError as ssl_error:
        print(f"SSL Error while connecting to Burp Suite: {ssl_error}")
        # Optionally, handle SSL errors here, for instance, retrying or logging them
    except RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # File path for the URLs
    url_file = "urls.txt"

    # Fetch URLs from the file
    urls = fetch_urls_from_file(url_file)
    
    # Loop through each URL and send the request
    for url in urls:
        send_request(url)
        time.sleep(1)  # Sleep to avoid overloading the proxy or server

if __name__ == "__main__":
    main()
