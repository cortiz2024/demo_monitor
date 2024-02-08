#!/bin/sh

# Load configuration from config.json
CONFIG_FILE="config.json"

# Read and parse the JSON configuration file
ENDPOINTS=$(jq -r '.endpoints | length' $CONFIG_FILE)

# Set initial health status
export HEALTH_STATUS="healthy"

# Infinite loop to make petitions
while true; do
    for i in $(seq 0 $(expr $ENDPOINTS - 1)); do
        # Get URL and interval_seconds for each endpoint
        URL=$(jq -r ".endpoints[$i].url" $CONFIG_FILE)
        INTERVAL_SECONDS=$(jq -r ".endpoints[$i].interval_seconds" $CONFIG_FILE)

        # Make the HTTP petition using cURL
        response_code=$(curl -s -o /dev/null -w "%{http_code}" $URL)
        echo "Response from $URL: $response_code"
        # Check if the response code indicates failure
        if [ "$response_code" != "200" ]; then
            echo "Petition to $URL failed."
            export HEALTH_STATUS="defected"
        fi
    done
    sleep $INTERVAL_SECONDS
done
