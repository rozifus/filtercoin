#!/usr/bin/env python

from __future__ import print_function
import urllib
from lxml.html import parse
from collections import defaultdict
import sys, os

TARGET = "http://www.cryptsy.com"

def autogen(site):
    data = defaultdict(list)

    raw = urllib.urlopen(TARGET)
    doc = parse(raw).getroot()
    matches = []
    matches += doc.cssselect("div#btc-markets ul li a")
    matches += doc.cssselect("div#ltc-markets ul li a")
    matches = [m.text_content().strip().split(" ")[0] for m in matches]
    matches = [m.split("/") for m in matches]
    for m in matches:
        data[m[1]].append(m[0])

    new_tags = {}

    return data



