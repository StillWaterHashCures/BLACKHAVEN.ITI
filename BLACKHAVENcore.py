#!/usr/bin/env python3
import os
import sys
import time
from colorama import Fore, Style, init
import pyfiglet
import subprocess

# Initialize colorama
init(autoreset=True)

# Framework Configuration
TOOL_ART = {
    'framework': pyfiglet.figlet_format("BLACKHAVEN", font="slant"),
    'ferox': pyfiglet.figlet_format("BLACKHAVEN", font="slant"),
    'nmap': pyfiglet.figlet_format("BLACKHAVEN", font="slant"),
    'enum4linux': pyfiglet.figlet_format("BLACKHAVEN", font="slant"),
    'netcat': pyfiglet.figlet_format("BLACKHAVEN", font="slant"),
}

TOOL_CREDITS = {
    'framework': "Intuitive Tooling Interface\nFramework Core Module\nAlpha Version 1.0\nMade by SWHC CerberKey",
    'ferox': "Intuitive Tooling Interface\nFeroxBuster Module\nAlpha Version 1.0\nMade by SWHC CerberKey",
    'nmap': "Intuitive Tooling Interface\nNmapScan Module\nAlpha Version 1.0\nMade by SWHC CerberKey",
    'enum4linux': "Intuitive Tooling Interface\nEnum4linux Module\nAlpha Version 1.0\nMade by SWHC CerberKey",
    'netcat': "Intuitive Tooling Interface\nNetcat Listener Module\nAlpha Version 1.0\nMade by SWHC CerberKey",
}

def show_banner(tool):
    print(Fore.YELLOW + Style.BRIGHT + TOOL_ART[tool])
    print(Fore.CYAN + TOOL_CREDITS[tool] + "\n")
    print(Fore.MAGENTA + "=" * 60 + Style.RESET_ALL)
    print(Fore.WHITE + f" Initialized at: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

def main_menu():
    os.system('clear' if os.name == 'posix' else 'cls')
    show_banner('framework')
    
    print(Fore.GREEN + "[1] Blackhaven Ferox - Web Enumeration")
    print(Fore.BLUE + "[2] Blackhaven Nmap - Network Scanning")
    print(Fore.MAGENTA + "[3] Blackhaven enum4linux - Windows/Linux Enumeration")
    print(Fore.WHITE + "[4] Blackhaven enum4linux-ng - Next-Gen Windows/Linux Enumeration")
    print(Fore.CYAN + "[5] Blackhaven Netcat - Listener Module")  # New option
    print(Fore.YELLOW + "[00] Run Dependency Loader")
    print(Fore.RED + "[0] Exit Framework\n")
    
    choice = input(Fore.CYAN + "[?] Select module: " + Style.RESET_ALL)
    return choice

def run_ferox_module():
    os.system('clear' if os.name == 'posix' else 'cls')
    show_banner('ferox')
    
    print(Fore.YELLOW + "[!] Type 'B' to back out to core module")
    target = input(Fore.CYAN + "[?] Enter target URL: " + Style.RESET_ALL)
    if target.upper() == 'B':
        return
    
    # Pass the target to the ferox module
    subprocess.run(['python3', 'BLACKHAVENferox.py', target])
    
    # Add your existing Feroxbuster code here
    print(Fore.YELLOW + "\n[+] Running Feroxbuster module...")
    time.sleep(2)
    print(Fore.GREEN + "[+] Scan completed successfully!")

def run_nmap_module():
    os.system('clear' if os.name == 'posix' else 'cls')
    show_banner('nmap')
    
    print(Fore.YELLOW + "[!] Type 'B' to back out to core module")
    target = input(Fore.CYAN + "[?] Enter target IP/host: " + Style.RESET_ALL)
    if target.upper() == 'B':
        return
    
    ports = input(Fore.CYAN + "[?] Ports to scan (default: 1-1000): ") or "1-1000"
    
    print(Fore.YELLOW + "\n[+] Initializing stealth scan...")
    cmd = f"nmap -sS -sV -p {ports} {target}"
    
    try:
        result = subprocess.run(cmd.split(), capture_output=True, text=True)
        print(Fore.GREEN + "\n[+] Scan results:")
        print(Fore.WHITE + result.stdout)
    except Exception as e:
        print(Fore.RED + f"[!] Scan failed: {str(e)}")

def run_enum4linux_module():
    os.system('clear' if os.name == 'posix' else 'cls')
    show_banner('enum4linux')
    
    print(Fore.YELLOW + "[!] Type 'B' to back out to core module")
    target = input(Fore.CYAN + "[?] Enter target IP: " + Style.RESET_ALL)
    if target.upper() == 'B':
        return
    
    # Pass the target to the enum4linux module as argument
    subprocess.run(['python3', 'BLACKHAVENenum4linux.py', target])

def run_enum4linux_ng_module():
    os.system('clear' if os.name == 'posix' else 'cls')
    show_banner('enum4linux')
    
    print(Fore.YELLOW + "[!] Type 'B' to back out to core module")
    target = input(Fore.CYAN + "[?] Enter target IP: " + Style.RESET_ALL)
    if target.upper() == 'B':
        return
    
    # Pass the target to the enum4linux-ng module as argument
    subprocess.run(['python3', 'BLACKHAVENenum4linux-ng.py', target])

def run_netcat_module():
    os.system('clear' if os.name == 'posix' else 'cls')
    show_banner('netcat')
    
    print(Fore.YELLOW + "[!] Type 'B' to back out to core module")
    port = input(Fore.CYAN + "[?] Enter port number (default 4444): " + Style.RESET_ALL) or "4444"
    if port.upper() == 'B':
        return
    
    try:
        port = int(port)
    except ValueError:
        print(Fore.RED + "❌ Invalid port number!" + Style.RESET_ALL)
        input(Fore.CYAN + "\n[Press Enter to continue...]" + Style.RESET_ALL)
        return
    
    # Pass the port to the netcat module
    subprocess.run(['python3', 'BLACKHAVENnetcat.py', str(port)])

def framework_loop():
    while True:
        choice = main_menu()
        
        if choice == '1':
            run_ferox_module()
            input(Fore.CYAN + "\n[Press Enter to continue...]" + Style.RESET_ALL)
        elif choice == '2':
            run_nmap_module()
            input(Fore.CYAN + "\n[Press Enter to continue...]" + Style.RESET_ALL)
        elif choice == '3':
            run_enum4linux_module()
            input(Fore.CYAN + "\n[Press Enter to continue...]" + Style.RESET_ALL)
        elif choice == '4':
            run_enum4linux_ng_module()
            input(Fore.CYAN + "\n[Press Enter to continue...]" + Style.RESET_ALL)
        elif choice == '5':  # New option
            run_netcat_module()
            input(Fore.CYAN + "\n[Press Enter to continue...]" + Style.RESET_ALL)
        elif choice == '00':
            run_loader()
            input(Fore.CYAN + "\n[Press Enter to continue...]" + Style.RESET_ALL)
        elif choice == '0':
            print(Fore.RED + "\n[!] Exiting the Blackhaven Framework...")
            break
        else:
            print(Fore.RED + "[!] Invalid selection!")
            time.sleep(1)
            
def run_loader():
    os.system('clear' if os.name == 'posix' else 'cls')
    show_banner('framework')
    
    print(Fore.YELLOW + "[!] Running dependency loader...")
    try:
        subprocess.run(['sudo', './BLACKHAVENloader.sh'], check=True)
    except subprocess.CalledProcessError:
        print(Fore.RED + "[!] Failed to run loader. Make sure you have sudo permissions.")
    except FileNotFoundError:
        print(Fore.RED + "[!] BLACKHAVENloader.sh not found in current directory.")

if __name__ == "__main__":
    try:
        framework_loop()
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Framework terminated by user!")
        sys.exit(0)