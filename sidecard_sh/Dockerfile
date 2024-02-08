# Use a base image
FROM alpine:latest

# Install required packages (curl and jq for JSON parsing)
RUN apk --no-cache add curl jq
WORKDIR /root/
# Copy the shell script and configuration file into the image
COPY check_ep.sh ./check_ep.sh
COPY config.json ./config.json

# Set the shell script as executable
RUN chmod a+x check_ep.sh

# Set the entry point to run the shell script
CMD ["sh","check_ep.sh"]
