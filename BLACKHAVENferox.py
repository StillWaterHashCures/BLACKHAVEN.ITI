#!/usr/bin/env python3
import subprocess
import time
from colorama import Fore, Style, init
import pyfiglet
import datetime
import sys

# Initialize colorama
init(autoreset=True)

def show_banner():
    """Display ASCII art banner"""
    banner = pyfiglet.figlet_format("BLACKHAVENferox", font='slant')
    print(f"{Fore.RED}{banner}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Made By SWHC Cerberkey{Style.RESET_ALL}")
    print("-" * 60 + "\n")

def run_ferox_scan(url, wordlist, scan_type):
    cmd = [
        "feroxbuster",
        "--url", url,
        "--wordlist", wordlist,
        "--no-state",
        "--dont-filter",
        "--quiet",
        "--filter-status", "404"  # Exclude 404 results
    ]

    if scan_type == "dir":
        cmd += ["--no-recursion", "--depth", "1"]
    elif scan_type == "page":
        cmd += ["--extensions", "php,html,asp"]
    elif scan_type == "dns":
        cmd += ["--dns"]

    print(Fore.YELLOW + "\n[+] Running feroxbuster with command:")
    print(Fore.WHITE + " ".join(cmd) + "\n")

    try:
        # Start the process
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True
        )

        start_time = time.time()
        timeout = 300  # 5 minutes
        results = []

        while True:
            # Calculate remaining time
            elapsed = time.time() - start_time
            remaining = max(0, timeout - elapsed)
            minutes = int(remaining // 60)
            seconds = int(remaining % 60)
            
            # Print countdown timer
            print(f"\r{Fore.CYAN}[⏰] Time remaining: {minutes:02d}:{seconds:02d}{Style.RESET_ALL}", end='', flush=True)

            # Check for timeout
            if elapsed >= timeout:
                process.terminate()
                print(Fore.YELLOW + "\n⏰ Scan timed out after 5 minutes")
                break

            # Read output line by line
            line = process.stdout.readline()
            if not line:
                if process.poll() is not None:
                    break
                continue

            # Only collect 200 and 301 results, explicitly excluding 404
            if '200' in line and '404' not in line:
                results.append((line.strip(), '200'))
            elif '301' in line and '404' not in line:
                results.append((line.strip(), '301'))

        # Print final results
        print("\n")  # New line after timer
        if not results:
            print(Fore.YELLOW + "⏰ No 200/301 results found after 5 minutes")
        else:
            print(Fore.GREEN + f"\n✅ Found {len(results)} valid results (200/301)")
            print("\nResults:")
            for line, status in results:
                if status == '200':
                    print(Fore.GREEN + line)
                elif status == '301':
                    print(Fore.YELLOW + line)

        return [r[0] for r in results], len(results)

    except Exception as e:
        print(Fore.RED + f"[!] Error: {str(e)}")
        return [], 0

def main():
    # Get target from command line argument if provided
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        print(Fore.YELLOW + "[!] Type 'B' to back out to core module")
        target = input(Fore.CYAN + "[?] Enter target URL: " + Style.RESET_ALL)
        if target.upper() == 'B':
            return  # This will return to the core module
    
    scan_sequence = [
        {
            "type": "dir",
            "name": "Directory Scan",
            "wordlist": "/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt"
        },
        {
            "type": "page",
            "name": "Page Scan",
            "wordlist": "/usr/share/seclists/Discovery/Web-Content/raft-medium-files.txt"
        },
        {
            "type": "dns",
            "name": "DNS Scan",
            "wordlist": "/usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt"
        }
    ]

    for scan in scan_sequence:
        print(Fore.BLUE + f"\n⚡ Starting {scan['name']}...")
        results, count = run_ferox_scan(
            target,
            scan["wordlist"],
            scan["type"]
        )
        
        print(Fore.GREEN + f"\n🕒 Found: {count} results")
        if not results:
            print(Fore.YELLOW + "No valid results found")

    print(Fore.GREEN + "\n✅ All scans completed!" + Style.RESET_ALL)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\n❌ Scan aborted by user!" + Style.RESET_ALL)
        sys.exit(1)