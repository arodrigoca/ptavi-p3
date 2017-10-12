#!/usr/bin/python3
# -*- coding: utf-8 -*-

from smallsmilhandler import SmallSMILHandler
import sys

if __name__ == "__main__":

	try:
		file = sys.argv[1]
		handler = SmallSMILHandler()
		text = handler.get_tags(file)
		print(len(text))

	except FileNotFoundError:
		print("Usage: python3 karaoke.py file.smil")
