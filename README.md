# BLACKHAVEN Framework
**Intuitive Tooling Interface**

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux-orange.svg)](https://www.linux.org/)

## 📋 Overview

The **BlackHaven Framework** is an Intuitive Tooling Interface designed to enhance penetration testing workflows through improved accessibility and streamlined tool integration. This interface provides a unified platform for existing red-team cybersecurity tools to create a efficient interface that bundles the most well-known tools & scripts in the industry.

So first and foremost i want to shoutout to the original creators and official owners of these tools:
- **Feroxbuster** Created by epi052 https://github.com/epi052/feroxbuster
- **Nmap** Created by Gordon Lyon (Fyodor) https://nmap.org/
- **Python-NMAP** Created by Alexandre Norman https://github.com/nmmapper/python3-nmap
- **enum4linux** Created by Mark Lowe https://github.com/CiscoCXSecurity/enum4linux
- **enum4linux-ng** Created by cddmp https://github.com/cddmp/enum4linux-ng
- **Netcat** Originally created by Hobbit https://nc110.sourceforge.io/
- **Samba Client** Created by the Samba Team https://www.samba.org/
- **LDAP Utils** Created by the OpenLDAP Project https://www.openldap.org/
- **NBTscan** Created by Alla Bezroutchko http://www.unixwiz.net/tools/nbtscan.html

## ⚠️ Important Usage Note

> **🚨 CRITICAL**  
> **ALWAYS** start the framework by running:
> ```bash
> python3 ./BLACKHAVENcore.py
> ```
> *(Improved CLI summon in the works!)*

This is the **ONLY** way to interact with the framework at the present moment. Running individual modules directly may cause system instability and scrambled output. The core module manages all interactions and ensures proper module execution.

## 🔧 Prerequisites

- **Python 3.8+** (verify with `python3 --version`)
- **Linux-based OS** (Kali/Parrot OS recommended)
- **sudo privileges** for dependency installation (Automated after password input!)

## 🧩 Core Components

| Module | Description |
|--------|-------------|
| **BLACKHAVENLoader.sh** | Install dependencies and modules<br>*(Automated first-time configuration and integrity checks)* |
| **BLACKHAVENferox.py** | Feroxbuster module<br>*(Simplified web directory brute-forcing interface)* |
| **BLACKHAVENnmap.py** | Nmap module<br>*(Python-NMAP integration with user-friendly interface)* |
| **BLACKHAVENcore.py** | Main operating module<br>*(Central menu system and module management)* |
| **BLACKHAVENenum4linux.py** | Windows/Linux Enumeration<br>*(Original enum4linux with simplified interface)* |
| **BLACKHAVENenum4linux-ng.py** | Next-Gen Enumeration<br>*(Enhanced version with JSON output support)* |
| **BLACKHAVENnetcat.py** | Netcat Listener Module<br>*(Simple port listener for callback management)* |

## 🚀 Installation

### 1. Repository Setup
```bash
git clone https://github.com/StillWaterHashCures/BLACKHAVEN.ITI.git
cd BLACKHAVEN.ITI
```

### 2. Virtual Environment (Recommended)
```bash
python3 -m venv .venv  # Isolate dependencies
source .venv/bin/activate
```

### 3. Permissions Setup
```bash
chmod +x *.py BLACKHAVENLoader.sh
```

## ⚙️ Initial Configuration

1. **Launch the framework:**
   ```bash
   python3 ./BLACKHAVENcore.py
   ```

2. **Select the dependencies installer (Option '00')**
   - Verifies and installs all required components
   - Automatically fixes missing/broken dependencies

## 📖 Usage

> **⚠️ IMPORTANT**  
> **ALWAYS** start the framework with:
> ```bash
> python3 ./BLACKHAVENcore.py
> ```

### Module Functionality:
- **Feroxbuster** - Web directory brute-forcing
- **Nmap** - Network scanning and service enumeration
- **enum4linux** - Windows/Linux SMB enumeration
- **enum4linux-ng** - Enhanced SMB enumeration
- **Netcat Listener** - Basic callback listener (port 4444 default)

## 📋 Operational Guidelines

### 1. Legal Compliance
- ✅ Only execute on authorized networks
- ✅ Maintain written testing consent

### 2. Best Practices
- Always use virtual environment:
  ```bash
  source .venv/bin/activate
  ```
- For listener modules, ensure proper firewall configuration

### 3. Debugging
- Run the Dependency installer in the Core Module (Option '00')
- This will verify and repair installation integrity
- For unresolved issues, contact via GitHub ([Cerberkey](https://github.com/Cerberkey))

## 🛠️ Troubleshooting

| Symptom | Solution |
|---------|----------|
| "Module not found" | Re-run `BLACKHAVENLoader.sh` |
| Permission errors | `chmod +x *.sh && sudo visudo` |
| Port conflicts | Verify `netstat -tulnp` output |
| Scrambled output | Always run through `BLACKHAVENcore.py` |
| Listener failures | Check firewall/AV configurations |

## ⚖️ Security Notice

> **🚨 WARNING**  
> Unauthorized use of this toolkit violates international cybercrime laws.  
> Ethical hacking requires explicit written permission from system owners.

All network activities are logged by default. Maintain proper documentation.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/StillWaterHashCures/BLACKHAVEN.ITI/issues)
- **Contact**: [Cerberkey](https://github.com/Cerberkey)

---

**Made with ❤️ for the cybersecurity community**