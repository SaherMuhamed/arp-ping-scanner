import time
from ipaddress import IPv4Network
import scapy.all as scapy
from utilities.vendor import VendorLookup


class NetworkScanner:

    def __init__(self, timeout=1, json_output=False):
        """
        Initializes the NetworkScanner instance.

        :param timeout: int, timeout for ARP requests
        :param json_output: bool, whether to output results in JSON format
        """
        self.ip_address = ""
        self.timeout = timeout
        self.json_output = json_output
        self.answered_devices = []
        self.vendor_lookup = VendorLookup(json_file_path="assets/mac-vendors-export.json")

    def scan_network(self, ip_address):
        """
        Scans the network for active devices.

        :param ip_address: str, IP range to scan (e.g., '192.168.1.0/24')
        """
        arp_request = scapy.ARP(pdst=ip_address)  # create an ARP request
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # broadcast an ARP packet to all devices in the network
        broadcast_arp_packets = broadcast / arp_request  # combine these 2 packets together to send

        start_time = time.time()  # start time for calculating scan duration

        answered, unanswered = scapy.srp(broadcast_arp_packets, timeout=self.timeout,
                                         verbose=False)  # send packets to all devices
        total_hosts = IPv4Network(ip_address, strict=False).num_addresses

        for sent_packet, received_packet in answered:
            vendor = self.vendor_lookup.get_vendor(mac_address=received_packet[scapy.Ether].src)
            print(f"{received_packet[scapy.ARP].psrc:<15}{received_packet[scapy.Ether].src:<20}{vendor}")
        print("")

        end_time = time.time()  # end time for calculating scan duration
        duration = end_time - start_time

        print(f"{len(answered)} packets received by filter, {len(unanswered)} packets dropped by kernel")
        print(f"Ending arp-ping v2.1.0: {total_hosts} hosts scanned in {duration:.3f} seconds ({total_hosts / duration:.2f} hosts/sec). {len(answered)} responded")
