#!/usr/bin/python3
# -*- coding: utf-8 -*-

from smallsmilhandler import SmallSMILHandler
import sys
import json
from urllib.request import urlretrieve
import os


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


def isHTTP(source):

    result = "http://" in source

    return result


def createFileName(source):

    workingDirectory = os.getcwd()
    nameStart = source.rfind("/") + 1
    newName = source[nameStart:]
    return newName


def downloadSource(source):

    try:
        newFile = createFileName(source)
        urlretrieve(source, newFile)

    except ValueError:
        pass


def getRemoteSources(tags):

    for tag in tags:
        try:
            source = tag['src']
            if isHTTP:
                downloadSource(source)

        except KeyError:
            pass


if __name__ == "__main__":

    try:
        file = sys.argv[1]
        handler = SmallSMILHandler()
        tags = handler.get_tags(file)
        printTags(tags)
        toJSON(tags, file)
        getRemoteSources(tags)

    except(FileNotFoundError, IndexError):
        print("Usage: python3 karaoke.py file.smil")
