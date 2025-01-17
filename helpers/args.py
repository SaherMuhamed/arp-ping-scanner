import netifaces
import ipaddress
from argparse import ArgumentParser


class UserArguments:
    def __init__(self):
        self.ip_range = None

    @staticmethod
    def args():
        parser = ArgumentParser(
            description="------- sARP Ping - Quickly Network Discovery Perform Active ARP Ping Scan -------")
        parser.add_argument(
            "-r", "--range", dest="ip_range",
            help="Specify an IP address range. Example: --range 192.168.1.0/24",
            type=str, required=True
        )
        options = parser.parse_args()
        if not options.ip_range:
            parser.error("[-] Please specify a valid IP address range. Example: --range 192.168.1.0/24")
        return options

    @staticmethod
    def get_interface_by_ip_range(ip_range):
        """
        Fetches the network interface, IP address, and MAC address that corresponds to the provided IP range.

        :param ip_range: str, IP range or address (e.g., '192.168.1.7')
        :return: dict containing interface name, IP address, and MAC address, or None if no match found.
        """
        try:
            # Parse the provided IP range (e.g., '192.168.1.0/24')
            ip_range_obj = ipaddress.ip_network(ip_range, strict=False)

            for interface in netifaces.interfaces():
                ip_info = netifaces.ifaddresses(interface).get(netifaces.AF_INET)
                if not ip_info or not isinstance(ip_info, list):
                    continue

                for addr in ip_info:
                    interface_ip = addr.get('addr')
                    if not interface_ip:
                        continue  # Skip if no valid IP address

                    netmask = addr.get('netmask', '255.255.255.255')
                    network = ipaddress.ip_network(f"{interface_ip}/{netmask}", strict=False)

                    # Check if the provided IP range overlaps with the interface's network
                    if ip_range_obj.overlaps(network):
                        mac_info = netifaces.ifaddresses(interface).get(netifaces.AF_LINK)
                        mac_address = mac_info[0]['addr'] if mac_info else "N/A"

                        return {
                            "interface": interface,
                            "ip_address": interface_ip,
                            "mac_address": mac_address
                        }

        except ValueError as ve:
            print(f"Invalid IP range: {ve}")
        except Exception as e:
            print(f"Error processing interface: {e}")

        return None
