#!/usr/bin/python3
# -*- coding: utf-8 -*-

from smallsmilhandler import SmallSMILHandler
import sys

def makeTagLines(tags):

	tagLine = ''
	tagLines = []

	for tag in tags:
		tagLine = tag['tag']
		for attribute in tag:
			if attribute != 'tag' and tag[attribute] != '':
				tagLine = tagLine + '\t' + attribute + '=' + tag[attribute]
		tagLines.append(tagLine)

	return tagLines

def printTags(tags):

	for element in makeTagLines(tags):
		print(element)


if __name__ == "__main__":

	try:
		file = sys.argv[1]
		handler = SmallSMILHandler()
		tags = handler.get_tags(file)
		printTags(tags)

	except (FileNotFoundError, IndexError):
		print("Usage: python3 karaoke.py file.smil")
