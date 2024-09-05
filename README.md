# AirRoot - Termux Root and Custom Prompt Tool

AirRoot is a Termux tool that helps you easily enable root access and customize your terminal prompt with a sleek modern design. If you don't have root, the tool will simulate a root environment and still give you a customized experience.

## Features:
- Automatically detects root access or simulates it if not available.
- Installs necessary root tools like `tsu` to enable root commands.
- Custom prompt with the AiRoot font and fish shell.
- Dynamically shows root or non-root prompt based on access.

## Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/AirSoftN/AirRoot.git
   cd AirRoot
   python root.py
   fish
   chsh -s /data/data/com.termux/files/usr/bin/bash
   
