![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  ![Kali](https://img.shields.io/badge/Kali-268BEE?style=for-the-badge&logo=kalilinux&logoColor=white)  ![Windows](https://img.shields.io/badge/Windows-0078D4.svg?style=for-the-badge&logo=Windows&logoColor=white)  ![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

This Python script allows you to scan a network and discover devices within a specified IP range. It uses Scapy, a powerful packet manipulation library, to send ARP request packets and capture responses from devices in the network. The script retrieves the IP address, MAC address, size of each packet, and hostname or vendor information for each discovered device.

## Prerequisites
- Python 3.x
- Required Python packages can be installed using the following command:
```commandline
pip install scapy requests
```

## Screenshots
- **For Linux:**<br><br>
![](https://github.com/SaherMuhamed/network-scanner-tool/blob/master/screenshots/Screenshot%202024-11-11-linux.png)

## Usage
1. Clone the repository or download the script to your local machine.
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Run the script with the following command:
```commandline
python3 arp-ping.py --range <IP_range>
```
4. Replace <IP_range> with the IP range you want to scan, e.g., 192.168.1.0/24.

## Output
The script generates a table displaying the following information for each discovered device:

- IP address
- MAC address
- Hostname or vendor information (obtained from an API)

## Example output:

### Updates
- `v1.0.1 - 27/12/2023` adding Size and improve scanning functionality
- `v1.1.0 - 11/11/2024` adding `--json or -j` optional switch to import the scan result into JSON format / increase scanning speed
- `v2.1.0 - 17/01/2025` huge changes, rename the project from *network scanner* => *arp-ping* also convert the project into OOP for further updating and releases & improve scanning functionality
