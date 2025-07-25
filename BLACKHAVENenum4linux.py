#!/usr/bin/env python3
import subprocess
import time
from colorama import Fore, Style, init
import pyfiglet
import datetime
import sys
import os
import re
import shutil

# Initialize colorama
init(autoreset=True)

def is_tool_installed(name):
    """Check if a tool is installed and available in PATH"""
    return shutil.which(name) is not None

def parse_enum4linux_output(output):
    """Parse enum4linux output and extract useful information"""
    results = {
        'users': [],
        'groups': [],
        'shares': [],
        'os_info': None,
        'domain_info': None
    }
    
    current_section = None
    
    for line in output.split('\n'):
        line = line.strip()
        
        if not line:
            continue
            
        # Detect section headers (more flexible matching)
        if "domain sid" in line.lower():
            current_section = 'domain'
        elif "enumerating users" in line.lower():
            current_section = 'users'
        elif "enumerating groups" in line.lower():
            current_section = 'groups'
        elif "enumerating shares" in line.lower():
            current_section = 'shares'
        elif "os information" in line.lower():
            current_section = 'os'
            
        # Parse content based on current section
        if current_section == 'users' and 'user:' in line.lower():
            user = re.search(r'user:\s*\[?(.*?)\]?', line, re.IGNORECASE)
            if user:
                results['users'].append(user.group(1).strip())
        elif current_section == 'groups' and 'group:' in line.lower():
            group = re.search(r'group:\s*\[?(.*?)\]?', line, re.IGNORECASE)
            if group:
                results['groups'].append(group.group(1).strip())
        elif current_section == 'shares' and 'share:' in line.lower():
            share = re.search(r'share:\s*\[?(.*?)\]?', line, re.IGNORECASE)
            if share:
                results['shares'].append(share.group(1).strip())
        elif current_section == 'os' and ('os:' in line.lower() or 'operating system:' in line.lower()):
            results['os_info'] = line.split(':')[1].strip()
        elif current_section == 'domain' and ('domain sid:' in line.lower()):
            results['domain_info'] = line.split(':')[1].strip()
            
    return results

def run_enum4linux_scan(target, options=None):
    """Run enum4linux scan with specified options"""
    if not is_tool_installed('enum4linux'):
        print(Fore.RED + "❌ enum4linux not found! Please install it first.")
        return None, 0
    
    cmd = ["enum4linux", target]
    
    if options:
        cmd.extend(options)
    
    print(Fore.BLUE + f"\n⚡ Starting enum4linux scan for {target}...")
    start_time = time.time()
    
    try:
        # Single process execution with output capture
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True
        )
        
        stdout_lines = []
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(Fore.WHITE + output.strip())
                stdout_lines.append(output)
        
        stderr = process.stderr.read()
        if stderr:
            print(Fore.RED + stderr)
        
        full_output = ''.join(stdout_lines)
        
        if process.returncode != 0:
            print(Fore.YELLOW + "\nEnum4linux finished with errors!")
            return None, time.time() - start_time
            
        results = parse_enum4linux_output(full_output)
        print(Fore.GREEN + "\nEnum4linux scan completed successfully!")
        return results, time.time() - start_time
        
    except Exception as e:
        print(Fore.RED + f"\n❌ Error during scan: {str(e)}")
        return None, time.time() - start_time

def sanitize_options(options_str):
    """Basic sanitization of custom options"""
    # Remove any potentially dangerous characters
    return [opt for opt in options_str.split() if opt.isalnum() or opt in ['-', '_']]

def main():
    # Check if target was passed as argument
    if len(sys.argv) > 1:
        target = sys.argv[1]
        print(Fore.GREEN + f"\n[+] Using target IP from arguments: {target}")
    else:
        # Fallback to prompt if no argument (for standalone use)
        target = input(Fore.CYAN + "[?] Enter target IP: " + Style.RESET_ALL)
        if target.upper() == 'B':
            return

    print(Fore.YELLOW + "\n[?] Select scan options:")
    print(Fore.WHITE + "[1] Basic scan (default)")
    print(Fore.WHITE + "[2] Comprehensive scan (all options)")
    print(Fore.WHITE + "[3] Custom options")
    
    choice = input(Fore.CYAN + "\n[?] Select option (1-3): " + Style.RESET_ALL).strip()
    
    options = None
    if choice == '2':
        options = ['-a']
    elif choice == '3':
        custom = input(Fore.CYAN + "[?] Enter custom options (space-separated): " + Style.RESET_ALL)
        options = sanitize_options(custom)

    results, duration = run_enum4linux_scan(target, options)
    
    if results:
        print(Fore.CYAN + f"\nScan completed in {duration:.2f} seconds")
        print(Fore.YELLOW + "\nResults Summary:")
        print(Fore.WHITE + f"Users: {', '.join(results['users']) if results['users'] else 'None found'}")
        print(Fore.WHITE + f"Groups: {', '.join(results['groups']) if results['groups'] else 'None found'}")
        print(Fore.WHITE + f"Shares: {', '.join(results['shares']) if results['shares'] else 'None found'}")
        print(Fore.WHITE + f"OS Info: {results['os_info'] or 'Not found'}")
        print(Fore.WHITE + f"Domain Info: {results['domain_info'] or 'Not found'}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\n❌ Scan aborted by user!" + Style.RESET_ALL)
        sys.exit(1)