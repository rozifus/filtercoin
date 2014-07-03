#!/usr/bin/env python

from __future__ import print_function
import sys, os
from lxml.html import etree, parse
import urllib


def process(data):
    for d in data:
        d["pop"] = getPop(d["href"])

if __name__ == '__main__':
    if sys.argv > 1:
        print(getPop(sys.argv[1]))




