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

    def getExchangePairs(info_page):

        raw = urllib.urlopen(info_page)
        doc = parse(raw).getroot()
        matches = doc.cssselect("table tbody tr td a")
        ex_pairs = [m.text_content() for m in matches[1:]]

        if len(ex_pairs) == 0:
            print("CCCGEN-WARNING: No trading pairs for ",
                  info_page.split("/")[-1])
        elif ex_pairs[0] == "Show logged in users..":
                ex_pairs = ex_pairs[1:]

        return ex_pairs

    print("___CCCGEN:GET_EXCHANGES___")

    raw = urllib.urlopen(EX_LIST)
    doc = parse(raw).getroot()

    matches = []
    matches += doc.cssselect("#tableMarkets tbody tr td a")
    matches = [EX_BASE + m.get("href") for m in matches]

    ex_data = {}
    for m in matches:
        ex_data[m.split("/")[-1]] = getExchangePairs(m)

    if "cccgen" in data.config.VERBOSE or "all" in data.config.VERBOSE:
        for e,p in ex_data.iteritems():
            print(e)
            print(p)
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




