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


def splitFileName(file):

    newFile = file.split(".")
    newFile = newFile[0]

    return newFile


def toJSON(tags, file):

    fileName = splitFileName(file)
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


class KaraokeLocal(SmallSMILHandler):

    def __init__(self, file):

        self.tags = self.get_tags(file)
        self.smilFile = file

    def __str__(self):

        printTags(self.tags)

    def to_json(self, smilName, jsonName=None):

        if jsonName is None:
            toJSON(self.tags, self.smilFile)

        else:
            with open(jsonName, "w") as f:
                json.dump(self.tags, f)

    def do_local(self):

        getRemoteSources(self.tags)


if __name__ == "__main__":

    try:
        file = sys.argv[1]
        # handler = SmallSMILHandler()
        # tags = handler.get_tags(file)
        # printTags(tags)
        # toJSON(tags, file)
        # getRemoteSources(tags)
        kar = KaraokeLocal(file)
        kar.__str__()
        kar.to_json(file)
        kar.do_local()
        kar.to_json(file, "local.json")
        kar.__str__()

    except(FileNotFoundError, IndexError):
        print("Usage: python3 karaoke.py file.smil")
