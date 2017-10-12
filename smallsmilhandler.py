#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

tags = []
#this are the lists of possible attributes for each tag
regList = ["id", "top", "left", "bottom", "right"]
rootList = ["width", "height", "background-color"]
imgList = ["src", "region", "begin", "dur"]
audList = ["src", "begin", "dur"]
textList = ["src", "region", "fill"]

def findAttValue(string, attrs):

	value = attrs.get(string, "")
	return value

def findAttrs(dictionary, listing, attrs):

	for attribute in listing:
		dictionary[attribute] = findAttValue(attribute, attrs)


class SmallSMILHandler(ContentHandler):


    def __init__ (self):
        """
        """

    def startElement(self, name, attrs):

        if name == 'root-layout':

        	rootDict = {'tag': name}
        	findAttrs(rootDict, rootList, attrs) 
        	tags.append(rootDict)

        elif name == 'region':

        	regDict = {'tag': name}
        	findAttrs(regDict, regList, attrs)
        	tags.append(regDict)

        elif name == 'img':

        	imgDict = {'tag': name}
        	findAttrs(imgDict, imgList, attrs)
        	tags.append(imgDict)

        elif name == 'audio':
            
            audDict = {'tag': name}
            findAttrs(audDict, audList, attrs)
            tags.append(audDict)

        elif name == 'textstream':

        	textDict = {'tag': name}
        	findAttrs(textDict, textList, attrs)
        	tags.append(textDict)

    def get_tags():

    	print(tags)
    	return tags

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(tags)