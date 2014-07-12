#!/usr/bin/env python

from __future__ import print_function
import urllib
from lxml.html import parse
from collections import defaultdict
import sys, os

TARGET = "http://www.btc-e.com"

def autogen():
    data = defaultdict(list)

    raw = urllib.urlopen(TARGET)
    doc = parse(raw).getroot()
    matches = []
    matches += doc.cssselect("p")
    matches = [m.text_content().strip().split(" ") for m in matches]
    #matches = [m.split("/") for m in matches]
    print(matches)
    for m in matches:
        data[m[1]].append(m[0])
    print(data)
    return data



