import socket
import sys
import logging
from ControllerTasks.Tasks.Task import Task
from scapy.all import *
from managers.Arguments import Arguments

class DHCPRequest(Task):

    def prepareImpl(self):
        pass

    def doTaskImpl(self):


        while self.status is Task.Status.RUNNING:
            try:
                sniff(iface=Arguments.getInterface(), prn = self.sniff_and_request, filter="port 67 and port 68", store=1)
                logging.getLogger('application').info('Message received')
            except Exception as e:
                print(e)

    def sniff_and_request(self, packet):
        try:
            if packet[IP].src != '0.0.0.0' and packet[Ether].dst != 'ff:ff:ff:ff:ff:ff':
                packetReceived = " Router MAC  : " + packet[Ether].src + "\nComputer MAC : " +packet[Ether].dst + "\nRouter IP: " +packet[IP].src + "\nIP offer to computer: " +packet[IP].dst
                logging.getLogger('application').info('/%s/', packetReceived)
                dhcp_request = (Ether(dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(chaddr=packet[Ether].dst)/DHCP(options=[("message-type","request"),("requested_addr", packet[IP].src),"end"]))
                sendp(dhcp_request, iface=Arguments.getInterface(), count=1)

        except Exception as e:
            print(e)
