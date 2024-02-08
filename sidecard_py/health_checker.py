import json
import requests
import time
import os

# Load configuration from config.json
CONFIG_FILE = "config.json"

# Read and parse the JSON configuration file
with open(CONFIG_FILE, 'r') as f:
    config = json.load(f)
    endpoints = config['endpoints']

# Set initial health status
os.environ['HEALTH_STATUS'] = "healthy"

# Infinite loop to make petitions
while True:
    for endpoint in endpoints:
        # Get URL and interval_seconds for each endpoint
        URL = endpoint['url']
        INTERVAL_SECONDS = endpoint['interval_seconds']

        # Make the HTTP request
        try:
            response = requests.get(URL)
            response_code = response.status_code
            print(f"Response from {URL}: {response_code}")

            # Check if the response code indicates failure
            if response_code != 200:
                print(f"Request to {URL} failed.")
                os.environ['HEALTH_STATUS'] = "defected"

        except Exception as e:
            print(f"Exception occurred while accessing {URL}: {str(e)}")
            os.environ['HEALTH_STATUS'] = "defected"

        time.sleep(INTERVAL_SECONDS)
