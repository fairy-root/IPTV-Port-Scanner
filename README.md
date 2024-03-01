### IPTV Port Scanner

```markdown
# IPTV Port Scanner

The IPTV Port Scanner is a specialized Python tool designed to help identify open network ports on IPTV systems. This utility is aimed at network administrators, security professionals, and IPTV service providers to ensure network security, compliance, and efficient service delivery by identifying accessible ports that could be potential vectors for unauthorized access or vulnerabilities.

## Features

- **Multiple Scanning Modes**: Offers various scanning strategies to accommodate different security assessment needs:
  1. **Standard Scan**: Covers ports from 1 to 1024, focusing on the most commonly used ports.
  2. **Extended Scan**: Expands the range up to 49152 to encompass additional services.
  3. **Well-Known Ports Scan**: Targets a curated list of ports known to be used by IPTV services and related applications.
  4. **Custom Port Scan**: Allows for targeted scanning of specific ports as defined by the user.
- **Multithreading Support**: Utilizes threading to speed up the scanning process, enabling rapid assessment of multiple ports simultaneously.
- **User-Friendly Output**: Leverages the `colorama` library for colored terminal output, enhancing readability of scan results.
- **Flexibility**: Users can specify targets and scanning modes through an interactive command-line interface.

## Installation

### Prerequisites

Ensure you have Python 3.x installed on your system. This script is compatible with various operating systems including Linux, Windows, and macOS.

### Installing Dependencies

The IPTV Port Scanner relies on the `colorama` package for colored output. Install all necessary dependencies by running:

```bash
pip install -r requirements.txt
```

This command will automatically fetch and install the latest version of `colorama`.

## Usage

To use the IPTV Port Scanner, follow these steps:

1. **Start the Script**: Run the script from your terminal or command prompt:

   ```bash
   python portscanner.py
   ```
   **it returns an output that can be used with Heartbleed vulnerability code**

2. **Enter Target IP Address**: When prompted, input the IP address of the IPTV system you wish to scan.

3. **Select Scanning Mode**: Choose one of the four scanning modes based on your assessment needs.

4. **Review Results**: The script will display the open ports and may suggest potential vulnerabilities or misconfigurations for further investigation.

### Scanning Modes Detailed

- **Mode 1 (Standard)**: Ideal for quick assessments, focusing on ports commonly used by various services.
- **Mode 2 (Extended)**: Comprehensive scanning, suitable for in-depth security audits.
- **Mode 3 (Well-Known Ports)**: Targets specific ports known to be significant for IPTV services, useful for focused assessments.
- **Mode 4 (Custom Port)**: Best for targeted scanning when investigating specific issues or following up on prior findings.

## IPTV Considerations

When scanning IPTV systems, be mindful of the potential impact on network performance and service availability. Always coordinate scanning activities with network administrators and conduct scans during maintenance windows or low-usage periods to minimize disruption.

## Legal Disclaimer

This IPTV Port Scanner is intended for educational, ethical hacking, and professional security assessment purposes only. Unauthorized scanning and testing of networks without explicit permission is illegal in many jurisdictions. It is the user's responsibility to comply with all applicable laws and regulations. The developers assume no liability for misuse or damages caused by this tool.