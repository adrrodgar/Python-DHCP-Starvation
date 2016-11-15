import os
import sys

class Arguments():

    args = None

    @staticmethod
    def config(args):
        Arguments.args = args

    @staticmethod
    def getInterface():
        return Arguments.args.interface

    @staticmethod
    def getCount():
        return Arguments.args.count     
