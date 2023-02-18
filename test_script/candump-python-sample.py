#!/usr/bin/env python3
# candump-python-sample.py

import sys
import string
import fileinput

def read_file():
	for line in fileinput.input():
		print(line, end="")
	#end for
#end def

if __name__=="__main__":
	read_file()
