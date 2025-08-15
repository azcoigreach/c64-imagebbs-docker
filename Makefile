# Makefile for C64 Image BBS Docker Environment

.PHONY: all up down disks enter-sysop export clean

# Default target
all: up

# Build and start the Docker containers in detached mode
up: disks
	@echo "Building and starting Docker services..."
	docker-compose build
	docker-compose up -d

# Stop and remove the Docker containers
down:
	@echo "Stopping and removing Docker services..."
	docker-compose down

# Build the C64 disk images from the submodule and seed files
disks:
	@echo "Creating C64 disk images inside the container..."
	docker-compose build vice
	docker-compose run --rm --entrypoint /bin/bash vice -c "chmod +x /work/scripts/make_disks.sh && /work/scripts/make_disks.sh"

# Attach to the running VICE container to access the C64 monitor/console
enter-sysop:
	@echo "Attaching to the VICE container's shell..."
	docker-compose exec vice /bin/bash

# Export the generated disk images to a timestamped directory
export:
	@echo "Exporting disk images..."
	@mkdir -p dist
	@tar -czvf dist/imagebbs-disks-$(shell date +%Y%m%d-%H%M%S).tar.gz -C disks .
	@echo "Disks exported to dist/"

# Clean up generated files
clean:
	@echo "Cleaning up generated files..."
	@rm -rf disks/*.d64 disks/*.d81 dist/
