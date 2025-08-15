#!/bin/bash
set -e

# Start xvfb in the background on display :99
Xvfb :99 -screen 0 1024x768x16 &

# Launch VICE using xvfb-run
# -config /work/configs/vice/vice.cfg: Use the pre-configured RS232 settings
# -autostart /work/disks/image_boot.d64: Load and run the BBS boot disk
# -8 /work/disks/image_boot.d64: Attach boot disk to drive 8
# -9 /work/disks/image_data.d81: Attach data disk to drive 9
xvfb-run --auto-servernum --server-args="-screen 0 1024x768x16" \
x64sc \
    -config /work/configs/vice/vice.cfg \
    -autostart /work/disks/image_boot.d64 \
    -8 /work/disks/image_boot.d64 \
    -9 /work/disks/image_data.d81
