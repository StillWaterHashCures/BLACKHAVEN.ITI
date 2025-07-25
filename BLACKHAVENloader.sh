#!/bin/bash

# ANSI color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

## ASCII Art Banner
echo -e "${RED}"
cat << "EOF"
    ____  __           __   __                                 
   / __ )/ ____ ______/ /__/ /_  ____ __   _____  ____  
  / __  / / __ `/ ___/ //_/ __ \/ __ `| | / / _ \/ __ \
 / /_/ / / /_/ / /__/ ,< / / / / /_/ /| |/ /  __/ / / /    
/_____/_/\__,_/\___/_/|_/_/ /_/\__,_/ |___/\___/_/ /_/
  
EOF
echo -e "${NC}"

# Print creator info
echo -e "${YELLOW}Dependency Loader/Installer${NC}\n"
echo -e "${YELLOW}Made by SWHC Cerberkey${NC}\n"

# Function to print status messages
print_status() {
    echo -e "${GREEN}[+]${NC} $1"
}

# Function to check if command was successful
check_status() {
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}[✓] Success${NC}"
    else
        echo -e "${RED}[✗] Failed${NC}"
        exit 1
    fi
}

# Check if script is run as root
if [ "$EUID" -ne 0 ]; then 
    echo -e "${RED}[!] Please run as root${NC}"
    exit 1
fi

# Print current working directory
print_status "Current working directory: $(pwd)"

# Update package list
print_status "Updating package list..."
apt update
check_status

# Install system packages
print_status "Installing system packages..."
apt install -y python3-pip python3-venv nmap enum4linux enum4linux-ng feroxbuster seclists netcat-traditional
check_status

# Check for virtual environment
if [ -z "$VIRTUAL_ENV" ]; then
    print_status "No virtual environment detected, checking if we need to create one..."
    if [ ! -d "venv" ]; then
        print_status "Creating virtual environment..."
        python3 -m venv venv
        check_status
    fi
    print_status "Activating virtual environment..."
    source venv/bin/activate
    check_status
else
    print_status "Using existing virtual environment: $VIRTUAL_ENV"
fi

# Upgrade pip in virtual environment
print_status "Upgrading pip in virtual environment..."
python3 -m pip install --upgrade pip
check_status

# Install Python packages in virtual environment
print_status "Installing Python packages in virtual environment..."
python3 -m pip install --no-cache-dir python-nmap colorama pyfiglet
check_status

# Verify all required tools are installed
print_status "Verifying installations..."
for tool in nmap enum4linux enum4linux-ng feroxbuster nc; do
    if ! command -v $tool &> /dev/null; then
        echo -e "${RED}[✗] $tool is not installed${NC}"
        exit 1
    else
        echo -e "${GREEN}[✓] $tool is installed${NC}"
    fi
done

# Verify Python packages
print_status "Verifying Python packages..."
python3 -c "import nmap, colorama, pyfiglet" 2>/dev/null
check_status

# Create a simple test script to verify installations
print_status "Creating test script..."
cat > test_imports.py << EOL
try:
    import nmap
    import datetime
    import argparse
    import sys
    import os
    import threading
    import logging
    from colorama import Fore, Style, init
    import time
    import pyfiglet
    print("All modules imported successfully!")
except ImportError as e:
    print(f"Error importing modules: {e}")
EOL

print_status "Testing imports..."
python3 test_imports.py
check_status

# Clean up test script
rm test_imports.py

echo -e "\n${GREEN}[✓] All dependencies installed successfully!${NC}"
echo -e "${YELLOW}[i] Virtual environment is active at: $VIRTUAL_ENV${NC}"
echo -e "${YELLOW}[i] To activate this environment in the future, run:${NC}"
echo -e "${GREEN}source venv/bin/activate${NC}"