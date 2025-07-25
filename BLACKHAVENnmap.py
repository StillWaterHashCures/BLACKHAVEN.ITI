#!/usr/bin/python3

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
import subprocess

# Initialize colorama for cross-platform colored output
init()

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                   format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def display_banner():
    """Display ASCII art banner"""
    banner = pyfiglet.figlet_format("BLACKHAVENnmap", font='slant')
    print(f"{Fore.RED}{banner}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Made By SWHC Cerberkey{Style.RESET_ALL}")
    print("-" * 60 + "\n")

class NmapScanner:
    def __init__(self, target, output_dir="scan_results", timeout=60):
        self.target = target
        self.output_dir = output_dir
        self.nm = nmap.PortScanner()
        self.timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.timeout = timeout
        self.open_ports = {}
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    # ... other methods remain unchanged ...

    def run_scan(self):
        log_file = self.create_log_file()
        
        self.print_and_log(f"\n[+] Starting Nmap Scan for: {self.target}", log_file, Fore.GREEN)
        self.print_and_log(f"[+] Scan started at: {self.timestamp}", log_file, Fore.GREEN)
        self.write_to_log(log_file, "-" * 50)

        try:
            # Run the combined scan with -sC -sV -O
            scan_args = '-sC -sV -O'
            self.print_and_log(f"[+] Running scan with arguments: {scan_args}", log_file, Fore.GREEN)
            
            self.nm.scan(self.target, arguments=scan_args)
            
            if self.nm.all_hosts():
                for host in self.nm.all_hosts():
                    try:
                        for proto in self.nm[host].all_protocols():
                            ports = sorted(self.nm[host][proto].keys())
                            for port in ports:
                                port_info = self.nm[host][proto][port]
                                if port_info.get('state') == 'open':
                                    self.open_ports[port] = port_info
                                
                                service = port_info.get('name', '')
                                state = port_info.get('state', '')
                                
                                port_detail = f"Port: {port}\tState: {state}\tService: {service}"
                                self.print_and_log(port_detail, log_file)
                    
                    except Exception as e:
                        print(f"{Fore.RED}[!] Error processing results: {str(e)}{Style.RESET_ALL}")
                        logger.error(f"Error processing results: {str(e)}")

        except Exception as e:
            error_msg = f"[-] An error occurred: {str(e)}"
            self.print_and_log(error_msg, log_file, Fore.RED)
            logger.error(error_msg)
        
        self.print_and_log(f"\n[+] Scan completed. Results saved to: {log_file}", log_file, Fore.GREEN)

def main():
    display_banner()
    
    print(Fore.YELLOW + "[!] Type 'B' to back out to core module")
    parser = argparse.ArgumentParser(description='Automated Nmap Scanner')
    parser.add_argument('-t', '--target', required=True, help='Target IP address or hostname')
    parser.add_argument('-o', '--output', default='scan_results', help='Output directory for scan results')
    parser.add_argument('--timeout', type=int, default=90, help='Timeout for individual scans in seconds')
    
    args = parser.parse_args()

    if args.target.upper() == 'B':
        return  # This will return to the core module

    try:
        scanner = NmapScanner(args.target, args.output, args.timeout)
        scanner.run_scan()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Scan interrupted by user{Style.RESET_ALL}")
        logger.warning("Scan interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Fore.RED}[!] An error occurred: {str(e)}{Style.RESET_ALL}")
        logger.error(f"Fatal error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()