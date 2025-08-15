#!/usr/bin/env python3
import os
import subprocess

# This script runs inside the Docker container, where the working dir is /work
REPO_ROOT = '/work'
DISKS_DIR = os.path.join(REPO_ROOT, 'disks')
SUBMODULE_DIR = os.path.join(REPO_ROOT, 'imagebbs3', 'image-bbs-v3.0')
CONFIG_SEED_DIR = os.path.join(REPO_ROOT, 'configs', 'seed')

# Disk image names
BOOT_DISK = os.path.join(DISKS_DIR, 'image_boot.d64')
DATA_DISK = os.path.join(DISKS_DIR, 'image_data.d81')

def run_c1541(disk_image, commands):
    """Helper to run c1541 with a set of commands."""
    # c1541 commands are passed via stdin to avoid complex shell quoting
    cmd_input = "\n".join(commands) + "\n"
    # Attach the disk image and execute commands from stdin
    subprocess.run(
        ['c1541'],
        input=f"attach {disk_image}\n{cmd_input}",
        text=True,
        check=True,
        cwd=REPO_ROOT # Run in repo root so c1541 can find the files
    )

def create_boot_disk():
    """Creates and populates the boot disk (.d64)."""
    print(f"Creating boot disk: {BOOT_DISK}")
    
    # Format the disk
    run_c1541(BOOT_DISK, [f'format "image-boot,ib" 0'])

    # Copy bootloader and system files
    # Paths must be relative to the CWD for c1541
    files_to_copy = {
        'imagebbs3/image-bbs-v3.0/program/1ST-BOOT.PRG': '1ST-BOOT',
        'imagebbs3/image-bbs-v3.0/program/2ND-BOOT.PRG': '2ND-BOOT',
        'imagebbs3/image-bbs-v3.0/program/3RD-BOOT.PRG': '3RD-BOOT',
        'imagebbs3/image-bbs-v3.0/program/IMAGE.PRG': 'IMAGE',
        'imagebbs3/image-bbs-v3.0/program/IMAGE-CFG.PRG': 'IMAGE-CFG',
        'imagebbs3/image-bbs-v3.0/program/IMAGE-SYSOP.PRG': 'IMAGE-SYSOP',
    }

    for src, dest in files_to_copy.items():
        print(f"Writing {src} to {BOOT_DISK} as {dest}")
        run_c1541(BOOT_DISK, [f'write "{src}" "{dest}"'])

def create_data_disk():
    """Creates and populates the data disk (.d81)."""
    print(f"Creating data disk: {DATA_DISK}")

    # Format the disk
    run_c1541(DATA_DISK, [f'format "image-data,id" 0'])
    
    print("Data disk created. Seeding with initial data is a future step.")


if __name__ == "__main__":
    os.makedirs(DISKS_DIR, exist_ok=True)
    # Create empty disk files first, as c1541 expects them to exist
    open(BOOT_DISK, 'a').close()
    open(DATA_DISK, 'a').close()
    
    create_boot_disk()
    create_data_disk()
    print("\nDisk creation complete.")
    print(f"Boot disk: {BOOT_DISK}")
    print(f"Data disk: {DATA_DISK}")
