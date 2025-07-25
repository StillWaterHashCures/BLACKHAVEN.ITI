BLACKHAVEN FRAMEWORK  
Intuitive Tooling Interface  
============================================================  

OVERVIEW  
------------------------------------------------------------  
The BlackHaven Framework is an Intuitive Tooling Interface designed to  
enhance penetration testing workflows through improved accessibility  
and streamlined tool integration. This interface provides a unified  
platform for security professionals to efficiently use the most well
known tools & scripts in the industry.

IMPORTANT USAGE NOTE
------------------------------------------------------------
!!! CRITICAL !!!
ALWAYS start the framework by running:
python3 ./BLACKHAVENcore.py
(improved CLI summon in the workings!)

This is the ONLY way to interact with the framework at the present moment. Running individual
modules directly may cause system instability and scrambled output.
The core module manages all interactions and ensures proper module execution.

PREREQUISITES  
------------------------------------------------------------  
- Python 3.8+ (verify with 'python3 --version')  
- Linux-based OS (Kali/Parrot OS recommended)  
- sudo privileges for dependency installation (Automated after password input!)

CORE COMPONENTS  
------------------------------------------------------------  
1. BLACKHAVENLoader.sh - Install dependencies and modules
   (Automated first-time configuration and integrity checks)
2. BLACKHAVENferox.py - Feroxbuster module
   (Simplified web directory brute-forcing interface)
3. BLACKHAVENnmap.py - Nmap module 
   (Python-NMAP integration with user-friendly interface)
4. BLACKHAVENcore.py - Main operating module
   (Central menu system and module management)
5. BLACKHAVENenum4linux.py - Windows/Linux Enumeration
   (Original enum4linux with simplified interface)
6. BLACKHAVENenum4linux-ng.py - Next-Gen Enumeration
   (Enhanced version with JSON output support)
7. BLACKHAVENnetcat.py - Netcat Listener Module
   (Simple port listener for callback management)

INSTALLATION  
------------------------------------------------------------  
1. REPOSITORY SETUP  
-------------------  
git clone https://github.com/your-repo/BlackHaven.git  
cd BlackHaven  

2. VIRTUAL ENVIRONMENT (RECOMMENDED)  
----------------------  
python3 -m venv .venv  # Isolate dependencies  
source .venv/bin/activate  

3. PERMISSIONS SETUP  
-------------------  
chmod +x *.py BLACKHAVENLoader.sh  

INITIAL CONFIGURATION  
------------------------------------------------------------  
1. Launch the framework:
   python3 ./BLACKHAVENcore.py 

2. Select the dependencies installer (Option '00')
   - Verifies and installs all required components
   - Automatically fixes missing/broken dependencies

USAGE  
------------------------------------------------------------  
!!! IMPORTANT !!!
ALWAYS start the framework with:
python3 ./BLACKHAVENcore.py

MODULE FUNCTIONALITY:
1. Feroxbuster - Web directory brute-forcing
2. Nmap - Network scanning and service enumeration  
3. enum4linux - Windows/Linux SMB enumeration  
4. enum4linux-ng - Enhanced SMB enumeration  
5. Netcat Listener - Basic callback listener (port 4444 default)

OPERATIONAL GUIDELINES  
------------------------------------------------------------  
1. LEGAL COMPLIANCE  
- Only execute on authorized networks  
- Maintain written testing consent  

2. BEST PRACTICES  
- Always use virtual environment:  
  source .venv/bin/activate  
- For listener modules, ensure proper firewall configuration

3. DEBUGGING
- Run the Dependency installer in the Core Module (Option '00')
  This will verify and repair installation integrity
- For unresolved issues, contact via GitHub (Cerberkey)

TROUBLESHOOTING  
------------------------------------------------------------  
Symptom                | Solution  
-----------------------|-------------------------------  
"Module not found"     | Re-run BLACKHAVENLoader.sh  
Permission errors      | chmod +x *.sh && sudo visudo  
Port conflicts         | Verify netstat -tulnp output  
Scrambled output       | Always run through BLACKHAVENcore.py  
Listener failures      | Check firewall/AV configurations  

SECURITY NOTICE  
------------------------------------------------------------  
!!! WARNING !!!  
Unauthorized use of this toolkit violates international cybercrime laws.  
Ethical hacking requires explicit written permission from system owners.  

All network activities are logged by default. Maintain proper documentation.