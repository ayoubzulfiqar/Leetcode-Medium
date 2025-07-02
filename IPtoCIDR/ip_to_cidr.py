import ipaddress
import sys

def ip_to_cidr(ip_address_str, mask_str):
    """
    Converts an IP address and a mask (prefix length or dotted decimal)
    to a CIDR network address string.
    """
    try:
        interface = ipaddress.IPv4Interface(f"{ip_address_str}/{mask_str}")
        return str(interface.network)
    except (ipaddress.AddressValueError, ipaddress.NetmaskValueError, ValueError):
        return None

if __name__ == "__main__":
    if len(sys.argv) == 3:
        ip_addr = sys.argv[1]
        mask = sys.argv[2]
        result = ip_to_cidr(ip_addr, mask)
        if result:
            print(result)