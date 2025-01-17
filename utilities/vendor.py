import json


class VendorLookup:
    def __init__(self, json_file_path):
        """
        Initializes the VendorLookup class with a path to the JSON file containing OUI data.

        :param json_file_path: str, path to the JSON file
        """
        self.oui_data = self._load_oui_data(json_file_path)

    @staticmethod
    def _load_oui_data(json_file_path):
        """
        Loads OUI data from the specified JSON file.

        :param json_file_path: str, path to the JSON file
        :return: list, OUI data loaded from the file
        """
        try:
            with open(json_file_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading OUI data: {e}")
            return []

    def get_vendor(self, mac_address):
        """
        Fetches the vendor information for a given MAC address from the local OUI data.

        :param mac_address: str, the MAC address to look up
        :return: str, the vendor name or 'Unknown' if not found
        """
        mac_prefix = mac_address.upper().replace(":", "")[:6]  # Extract the first 6 characters of the MAC
        for entry in self.oui_data:
            if entry.get("macPrefix", "").replace(":", "").upper() == mac_prefix:
                return entry.get("vendorName", "Unknown")
        return "Unknown"
