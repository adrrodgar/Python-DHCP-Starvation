import socket
import sys
import logging
from ControllerTasks.Tasks.Task import Task
import string
from scapy.all import *
from managers.Arguments import Arguments

class DHCPdiscover(Task):

    def prepareImpl(self):
        pass

    def doTaskImpl(self):

        try:
            MACs_list = self.mac_list()
            for mac in MACs_list:
                conf.checkIPaddr = False
                dhcp_discover = Ether(dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(chaddr=mac)/DHCP(options=[("message-type","discover"),"end"])
                sendp(dhcp_discover, iface=Arguments.getInterface(), count=1)
        except Exception as e:
            print(e)

    def mac_list(self):

        MAClist = []
        for x in range(0,Arguments.getCount()):
            unique_hexdigits = str.encode("".join(set(string.hexdigits.lower())))
            MAClist.append(RandString(12, unique_hexdigits))
        return MAClist
