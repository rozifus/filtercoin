#!/usr/bin/env python

from __future__ import print_function
import sys, os
import urllib
from lxml.html import parse
import modules.readwrite as rw


EX_BASE = "http://www.cryptocoincharts.info"
EX_LIST = EX_BASE + "/v2/markets/info"
EX_SHOW = EX_BASE + "v2/markets/show/"

def getExchanges(data):

    raw = urllib.urlopen(EX_LIST)
    doc = parse(raw).getroot()

    matches = []
    matches += doc.cssselect("#tableMarkets tbody tr td a")
    matches = [EX_BASE + m.get("href") for m in matches]

    if "cccgen" in data.config.VERBOSE or "all" in data.config.VERBOSE:
        print("___CCCGEN:GET_EXCHANGES___")
        for m in matches:
            print(m)
        print("--------------------------")


def process(data):

    exs = getExchanges(data)
    print(exs)

    """
    for site in sites:
        if "cccg" in site:
            path = "modules.cccgen." + site["cccg"]
            sub_module = None
            sub_module = __import__(path, fromlist=["gen"])
            sub_module.gen(site)
            del site["cccg"]
    """




