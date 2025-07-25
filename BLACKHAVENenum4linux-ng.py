#!/usr/bin/env python3
import subprocess
import time
from colorama import Fore, Style, init
import pyfiglet
import datetime
import sys
import shutil
import os
import re
import json

# Initialize colorama
init(autoreset=True)

def is_tool_installed(name):
    """Check if enum4linux-ng is available"""
    return shutil.which(name) is not None

def parse_enum4linux_ng_output(output):
    """Parse enum4linux-ng output and extract useful information"""
    try:
        # Try to parse as JSON first
        data = json.loads(output)
        return {
            'users': data.get('users', []),
            'groups': data.get('groups', []),
            'shares': data.get('shares', []),
            'os_info': data.get('os_info', None),
            'domain_info': data.get('domain_info', None)
        }
    except json.JSONDecodeError:
        # Fallback to text parsing if JSON fails
        results = {
            'users': [],
            'groups': [],
            'shares': [],
            'os_info': None,
            'domain_info': None
        }
        
        for line in output.split('\n'):
            line = line.strip()
            if not line:
                continue
                
            if 'User:' in line:
                user = re.search(r'User:\s*(.*)', line)
                if user:
                    results['users'].append(user.group(1))
            elif 'Group:' in line:
                group = re.search(r'Group:\s*(.*)', line)
                if group:
                    results['groups'].append(group.group(1))
            elif 'Share:' in line:
                share = re.search(r'Share:\s*(.*)', line)
                if share:
                    results['shares'].append(share.group(1))
            elif 'OS:' in line:
                results['os_info'] = line.split('OS:')[1].strip()
            elif 'Domain SID:' in line:
                results['domain_info'] = line.split('Domain SID:')[1].strip()
                
        return results

def run_enum4linux_ng_scan(target, options=None):
    """Run enum4linux-ng scan with specified options"""
    if not is_tool_installed('enum4linux-ng'):
        print(Fore.RED + "❌ enum4linux-ng not found! Please install it first.")
        return None, 0
    
    cmd = ["enum4linux-ng", target, "-oJ", "-"]
    
    if options:
        cmd.extend(options)
    
    print(Fore.BLUE + f"\n⚡ Starting enum4linux-ng scan for {target}...")
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
            print(Fore.YELLOW + "\nEnum4linux-ng finished with errors!")
            return None, time.time() - start_time
            
        results = parse_enum4linux_ng_output(full_output)
        print(Fore.GREEN + "\nEnum4linux-ng scan completed successfully!")
        return results, time.time() - start_time
        
    except Exception as e:
        print(Fore.RED + f"[!] Error: {str(e)}")
        return None, time.time() - start_time

def sanitize_options(options_str):
    """Basic sanitization of custom options"""
    return [opt for opt in options_str.split() if opt.replace('-', '').isalnum()]

def main():
    # Check for target passed as argument
    if len(sys.argv) > 1:
        target = sys.argv[1]
        print(Fore.GREEN + f"\n[+] Using target IP from arguments: {target}")
    else:
        # Fallback to prompt if no argument (for standalone use)
        target = input(Fore.CYAN + "[?] Enter target IP (or 'B' to go back): " + Style.RESET_ALL)
        if target.upper() == 'B':
            return
    
    print(Fore.YELLOW + "\n[?] Select scan options:")
    print(Fore.WHITE + "[1] Basic scan (default)")
    print(Fore.WHITE + "[2] Comprehensive scan (all options)")
    print(Fore.WHITE + "[3] Custom options")
    
    choice = input(Fore.CYAN + "\n[?] Select option (1-3): " + Style.RESET_ALL).strip()
    
    options = None
    if choice == '2':
        options = ['-A']
    elif choice == '3':
        custom = input(Fore.CYAN + "[?] Enter custom options (space-separated): " + Style.RESET_ALL)
        options = sanitize_options(custom)
    
    results, duration = run_enum4linux_ng_scan(target, options)
    
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