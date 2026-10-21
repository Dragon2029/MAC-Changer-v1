#!/usr/bin/env python

# there are libraries
import subprocess as sub
import optparse
import re
# ------------------------------------------------------
# this is function response for get arguments from user:
def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--iface", dest='iface', help='Interface to change its MAC address')
    parser.add_option("-m", "--mac", dest='new_mac', help='Type new MAC address')

    return parser.parse_args()

# ---------------------------------------------------------------------
# this is function response for change MAC address to new MAC address
def change_mac(iface, new_mac):
    print(f"[+] Changing MAC address for {iface} to {new_mac}")
    sub.call(['ifconfig', iface, 'down'])
    sub.call(['ifconfig', iface, 'hw', 'ether', new_mac])
    sub.call(['ifconfig', iface, 'up'])

# this is function get current MAC address from ifconfig:
def get_current_mac(iface):

    ifconfig_result = sub.check_output(["ifconfig", iface], text=True)

    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)

    else:
        print("[-] Could not read MAC address.")


(options, arguments) = get_arguments()

# Get Current MAC from ifconfig command
current_mac = get_current_mac(options.interface)
print(f"Current MAC = {current_mac}")

# Changed MAC Address To New MAC Address
change_mac(options.interface, options.new_mac)

# Get current MAC from ifconfig command after changed.
current_mac = get_current_mac(options.interface)

# Check on current MAC
if current_mac == options.new_mac:
    print(f"[+] MAC address was successfully changed to [{current_mac}].")
else:
    print(f"[-] MAC address did not get changed [{current_mac}].")