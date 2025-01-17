#!/usr/bin/env python3

import sys
from helpers.args import UserArguments
from utilities.scan import NetworkScanner

if sys.version_info < (3, 0):
    sys.stderr.write("\nYou need python 3.0 or later to run this script\n")
    sys.stderr.write("Please update and make sure you use the command python3 arp-ping.py -r <ip/24>\n\n")
    sys.exit(0)

option = UserArguments()
scanner = NetworkScanner()


def main():
    print(
        f"Interface: {option.get_interface_by_ip_range(ip_range=option.args().ip_range)['interface']}, "
        f"MAC: {option.get_interface_by_ip_range(ip_range=option.args().ip_range)['mac_address']}, "
        f"IPv4: {option.get_interface_by_ip_range(ip_range=option.args().ip_range)['ip_address']}"
    )
    print("Starting arp-ping v2.1.0 with 256 hosts (https://github.com/SaherMuhamed/arp-ping-scanner)")
    scanner.scan_network(ip_address=option.args().ip_range)  # start scan the target network


if __name__ == "__main__":
    main()
