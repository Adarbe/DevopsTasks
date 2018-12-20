#IP and Submask
#---------------#

import ipaddress

def IsIpInSubnet(ipAddress, subnet):
    return ipaddress.ip_address(ipAddress) in ipaddress.ip_network(subnet)

print(IsIpInSubnet('192.168.0.1', '192.168.0.0/24'))