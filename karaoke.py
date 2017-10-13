#!/usr/bin/python3
# -*- coding: utf-8 -*-

from smallsmilhandler import SmallSMILHandler
import sys
import json

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

def splitFileName():

	file = sys.argv[1].split(".")
	file = file[0]

	return file 

def toJSON(tags, file):

	fileName = splitFileName()
	fileName = fileName + '.json'

	with open(fileName, "w") as f:
		json.dump(tags, f)



if __name__ == "__main__":

	try:
		file = sys.argv[1]
		handler = SmallSMILHandler()
		tags = handler.get_tags(file)
		printTags(tags)
		toJSON(tags, file)

	except (FileNotFoundError, IndexError):
		print("Usage: python3 karaoke.py file.smil")
