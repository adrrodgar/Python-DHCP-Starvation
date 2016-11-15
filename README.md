# Python-DHCP-Starvation

This project help you to upload files to your own cluster of S3.

## Install

The recommended versions of Python for use with this client is Python 2.7.

### From PyPI

The requeriments are:
* scapy library

You can install scapy from PyPI

```
pip install scapy
```

## Testing

In first place, it's necessary know the script arguments.
* -h: help.
* -c: count, number of address to consume.
* -i: interface, network interface to use.
* Default: 200 IP address to consume and use eth0 network interface.

Execute the script.

```
python dhcpAttack.py -c 200 -i eth0
```
