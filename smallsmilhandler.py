#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

tags = {
    'root-layout': [],
    'region': [],
    'img': [],
    'audio': [],
    'textstream': []
}


class SmallSMILHandler(ContentHandler):
    """
    Class to handle bad puns
    """

    def __init__ (self):
        """
        """

    def startElement(self, name, attrs):

        if name == 'root-layout':
            """
            tags['root-layout'].append(attrs.get('width', ""))
            print(tags['root-layout'])
            """
            pass
        elif name == 'region':
            pass
        elif name == 'img':
            pass
        elif name == 'audio':
            pass
        elif name == 'textstream':
            pass


if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
