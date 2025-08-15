# Dockerfile for tcpser
# This builds tcpser from source.

FROM ubuntu:22.04

# Install build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy the tcpser source code into the container
COPY ./tcpser-src /app/tcpser-src

# Build tcpser directly from its root Makefile
RUN make -C /app/tcpser-src

# Set the entrypoint to the compiled tcpser binary
ENTRYPOINT ["/app/tcpser-src/tcpser"]
