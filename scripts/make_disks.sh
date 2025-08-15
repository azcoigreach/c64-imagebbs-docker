#!/bin/bash
set -e

# This script runs inside the Docker container, where the working dir is /work
REPO_ROOT="/work"
SCRIPTS_DIR="$REPO_ROOT/scripts"
DISKS_DIR="$REPO_ROOT/disks"

# Ensure the disks directory exists
mkdir -p "$DISKS_DIR"

# Create disk images
echo "Creating disk images..."
python3 "$SCRIPTS_DIR/import_from_submodule.py"

echo "Disk images created successfully in $DISKS_DIR"
