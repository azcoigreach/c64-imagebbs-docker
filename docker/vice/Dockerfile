# Base on Ubuntu LTS for better package availability
FROM ubuntu:22.04

# Set frontend to noninteractive to avoid prompts during build
ENV DEBIAN_FRONTEND=noninteractive

# Install VICE, xvfb (for headless operation), python and required libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    vice \
    xvfb \
    python3 \
    libsdl2-2.0-0 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set up the working directory
WORKDIR /work

# Copy the entrypoint script and make it executable
COPY docker/vice/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# The entrypoint will launch VICE
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
