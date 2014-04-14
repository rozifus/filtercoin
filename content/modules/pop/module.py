#!/usr/bin/env python

from __future__ import print_function
import sys, os
from lxml.html import etree, parse
import urllib
import modules.readwrite as rw

POP_SITE_BASE = "http://www.trafficestimate.com"
TAR_S = "has received an estimated"
TAR_E = "visits over the last"

def stripUrl(url):
    pro = url.find("://")
    if pro > 0:
        url = url[pro+3:]
    slash = url.find("/")
    if slash > 0:
        url = url[:slash]
    return url

def getPop(url):
    surl = stripUrl(url)
    surl = POP_SITE_BASE + '/' + surl
    print(surl)
    raw = urllib.urlopen(surl)
    doc = parse(raw).getroot()
    matches = doc.find_class('chart-yoy') + \
              doc.find_class('profile-section-desc')
    text_dump = reduce(lambda x,y: x+" "+y,
                    map(lambda m: m.text_content(),
                        matches), "")
    s,e = text_dump.find(TAR_S), text_dump.find(TAR_E)
    if s == -1 or e == -1:
        print("No matches:" + url)
        return 0
    return int(text_dump[s+len(TAR_S):e].replace(',',''))

def process(data):
    for d in data:
        d["pop"] = getPop(d["href"])

if __name__ == '__main__':
    if sys.argv > 1:
        print(getPop(sys.argv[1]))




