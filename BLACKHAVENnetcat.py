#!/usr/bin/env python3
import subprocess
import time
from colorama import Fore, Style, init
import pyfiglet
import sys

# Initialize colorama
init(autoreset=True)

def run_netcat_listener(port=4444):
    """Run netcat listener on specified port"""
    try:
        print(Fore.BLUE + f"\n⚡ Starting Netcat listener on port {port}...")
        print(Fore.YELLOW + "[!] Press Ctrl+C to stop the listener")
        
        # Run netcat listener
        cmd = ["nc", "-lvnp", str(port)]
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True
        )
        
        # Print output in real-time
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(Fore.WHITE + output.strip())
        
        return True
    
    except KeyboardInterrupt:
        print(Fore.RED + "\n❌ Listener stopped by user!" + Style.RESET_ALL)
        return False
    except Exception as e:
        print(Fore.RED + f"\n❌ Error: {str(e)}" + Style.RESET_ALL)
        return False

def main():
    # Check if port was passed as argument
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = input(Fore.CYAN + "[?] Enter port number (default 4444): " + Style.RESET_ALL) or "4444"
    
    try:
        port = int(port)
    except ValueError:
        print(Fore.RED + "❌ Invalid port number!" + Style.RESET_ALL)
        return
    
    run_netcat_listener(port)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\n❌ Operation aborted by user!" + Style.RESET_ALL)
        sys.exit(1)