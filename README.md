# MAC Address Changer

This script is designed to change the MAC address of a specified network interface. It is created for educational purposes to demonstrate the use of Python libraries `optparse` and `subprocess`.

## Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Disclaimer](#disclaimer)
- [Links](#links)

## Introduction

The MAC Address Changer script allows you to change the MAC address of your network interface using Python. This can be useful for testing network configurations, enhancing privacy, and other purposes.

## Requirements

- Python 3.x
- Appropriate permissions to change network settings (usually root or administrator)

## Installation

Clone this repository to your local computer:

```sh
git clone https://github.com/my-holber/linux_mac-address-changer.git
```
## Usage

Run the script with the necessary options:
```
sudo python mac_changer.py -i eth0 -m 00:11:22:33:44:55
```
This will change the MAC address of the eth0 interface to 00:11:22:33:44:55.


## Disclaimer

This script is intended for educational purposes only. Changing your MAC address can have unintended consequences and may violate your network provider's policy. Use this script responsibly and at your own risk.

## Links
- [Documentation optparse](https://docs.python.org/3/library/optparse.html)
- [Documentation subprocess](https://docs.python.org/3/library/subprocess.html) 
