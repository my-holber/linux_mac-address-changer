#!/usr/bin/env python

import subprocess
import optparse


def get_arguments():
    """
    Parses and returns command-line arguments.
    Checks for necessary arguments and displays an error if they are missing.
    """
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='Interface to change its MAC address')
    parser.add_option('-m', '--mac', dest='new_mac', help='New MAC address')
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC address, use --help for more info.")
    return options


def change_mac(interface, new_mac):
    """
    Changes the MAC address of the specified network interface.
    """
    print("[+] Changing MAC address for", interface, "to", new_mac)
    subprocess.run(['ifconfig', interface, 'down'], capture_output=True, text=True)
    subprocess.run(['ifconfig', interface, 'hw', 'ether', new_mac], capture_output=True, text=True)
    subprocess.run(['ifconfig', interface, 'up'], capture_output=True, text=True)

'''Get command-line arguments'''
options = get_arguments()
'''Change the MAC address of the specified interface'''
change_mac(options.interface, options.new_mac)
