#!/usr/bin/env python3

import subprocess as sub
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--iface", dest='iface', help='Interface to change its MAC address')
    parser.add_option("-m", "--mac", dest='new_mac', help='Type new MAC address')
    (options, arguments) = parser.parse_args()

    if not options.iface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    if not options.new_mac:
        parser.error("[-] Please specify a new MAC address, use --help for more info.")

    return options

def change_mac(iface, new_mac):
    print(f"[+] Changing MAC address for {iface} to {new_mac}")
    sub.call(['ifconfig', iface, 'down'])
    sub.call(['ifconfig', iface, 'hw', 'ether', new_mac])
    sub.call(['ifconfig', iface, 'up'])

def get_current_mac(iface):
    try:
        ifconfig_result = sub.check_output(["ifconfig", iface], text=True)
    except sub.CalledProcessError:
        print(f"[-] Could not find interface {iface}")
        return None

    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")
        return None

options = get_arguments()

current_mac = get_current_mac(options.iface)
print(f"[+] Current MAC = {current_mac}")

change_mac(options.iface, options.new_mac)

current_mac = get_current_mac(options.iface)

if current_mac == options.new_mac:
    print(f"[+] MAC address was successfully changed to [{current_mac}].")
else:
    print(f"[-] MAC address did not get changed [{current_mac}].")