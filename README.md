# C64 Image BBS Docker Development Environment

This repository provides a Docker-based development environment for the Image BBS v3.0 for the Commodore 64. It allows you to run the BBS in an emulator (VICE) with telnet access, modify its configuration, and build disk images that can be deployed on real C64 hardware.

The core Image BBS source code is included as a git submodule, tracking the official repository.

## Quickstart

1.  **Clone the repository and initialize submodules:**
    ```bash
    git clone https://github.com/azcoigreach/c64-imagebbs-docker.git
    cd c64-imagebbs-docker
    git submodule update --init --recursive
    ```

2.  **Build the disk images:**
    This step uses `c1541` (from VICE) to create the `.d64` and `.d81` disk images from the `imagebbs3` submodule.
    ```bash
    make disks
    ```

3.  **Start the services:**
    This will build the Docker containers and start `tcpser` and `vice`.
    ```bash
    make up
    ```

4.  **Connect to the BBS:**
    Once the services are running, you can connect to your BBS via telnet.
    ```bash
    telnet localhost 6400
    ```

## Development Workflow

### Updating the BBS Core

To pull the latest changes from the `ImageBBS3` submodule:

```bash
git submodule update --remote
make disks
make up
```

This will fetch the latest version of the BBS software, rebuild the disk images with the new files, and restart the Docker services.

### Accessing the VICE Emulator

You can attach to the running VICE container to get access to the C64 monitor and file system:

```bash
make enter-sysop
```

### Moving to Real Hardware

The disk images generated in the `disks/` directory (`image_boot.d64` and `image_data.d81`) are standard C64 disk images. They can be written to real floppy disks or used with modern hardware solutions like an SD2IEC, Pi1541, or Ultimate 64.

To deploy on hardware, you will need a way to handle the modem connection. Options include:

*   **WiModem64:** A hardware modem that connects to your Wi-Fi and emulates a Hayes modem.
*   **Ultimate 64:** The Ethernet port on an Ultimate 64 can be used with specific software to handle telnet connections.
*   **Raspberry Pi:** A Raspberry Pi can run `tcpser` on your local network to act as a bridge between the internet and your C64's serial port.

The configuration of Image BBS for these options is outside the scope of this document, but the core message bases, user data, and system files on the disks will be the same.

## Makefile Targets

*   `make up`: Build and start the Docker services.
*   `make down`: Stop and remove the Docker services.
*   `make disks`: Generate the `.d64` and `.d81` disk images.
*   `make enter-sysop`: Attach to the running VICE container.
*   `make export`: Create a timestamped archive of the disk images in the `dist/` directory.
*   `make clean`: Remove generated disk images and exported archives.
