import requests
import time

def make_requests(url, num_requests):
    for i in range(num_requests):
        try:
            response = requests.get(url)
            print(f"Request {i+1}/{num_requests} - Status Code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Request {i+1}/{num_requests} - Error: {e}")

        # Delay between requests to avoid overwhelming the server
        time.sleep(0.5)

if __name__ == "__main__":
    website_url = "http://exotikalhub.com/"  # Replace with the URL of the website you want to analyze
    num_requests = 10000  # Number of requests to be made

    make_requests(website_url, num_requests)
