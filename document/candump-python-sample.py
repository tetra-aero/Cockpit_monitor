#!/usr/bin/env python3
"""candump-python-sample.py
receive VCAN0 data and print it to stdout

- Usage
$ python3 candump-python-sample.py
"""
#__all__ = ['sys']
__author__ = "Yoshihiro Nakagawa <yoshihiro.nakagawa@tetra-aviation.com>"
__date__ = "26 October 2023"

__version__ = "1.0.0"
__credits__ = "teTra Aviation Corp."


import sys
import string
import fileinput
import can

def read_file():
        for line in fileinput.input():
                print(line, end="")
        #end for
#end def

if __name__=="__main__":
    #read_file()
    bus_vcan0 = can.interface.Bus(channel='vcan0', bustype='socketcan', bitrate=125000, canfilters=None)
    try:
        for msg in bus_vcan0:
            print(msg)
        #end for
    except KeyboardInterrupt:
        print("exit")
        bus_vcan0.shutdown()
    #end try
