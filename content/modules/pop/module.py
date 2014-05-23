#!/usr/bin/env python

from __future__ import print_function
import sys, os
import math, random
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
    raw = urllib.urlopen(surl)
    doc = parse(raw).getroot()
    matches = doc.find_class('chart-yoy') + \
              doc.find_class('profile-section-desc')
    text_dump = reduce(lambda x,y: x+" "+y,
                    map(lambda m: m.text_content(),
                        matches), "")
    s,e = text_dump.find(TAR_S), text_dump.find(TAR_E)
    if s == -1 or e == -1:
        return 0
    return int(text_dump[s+len(TAR_S):e].replace(',',''))

def process(data):

    print()
    print("--------------")
    print("| POP_MODULE |")
    print("--------------")

    print()
    print(":FETCH_SITE_POP")

    zero, non_zero = 0.0,0.0
    for d in data.sites:
        href = d["href"]
        pop = getPop(href)
        if pop == 0:
            zero += 1
            pop = random.random()
        else:
            non_zero += 1
            pop = math.log10(pop)
        pop = round(pop, 2)
        d["pop"] = pop
        if "all" in data.config.VERBOSE or "pop" in data.config.VERBOSE:
            print()
            print(href)
            print(pop)

    if zero > non_zero:
        print()
        print("WARNING: more than half sites returned zero pop")


if __name__ == '__main__':
    if sys.argv > 1:
        print(getPop(sys.argv[1]))




