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

        if ex_pairs and ex_pairs[0] == "Show logged in users..":
            ex_pairs = ex_pairs[1:]

        return ex_pairs

    print(":GET_EXCHANGES")

    raw = urllib.urlopen(EX_LIST)
    doc = parse(raw).getroot()

    matches = []
    matches += doc.cssselect("#tableMarkets tbody tr td a")
    matches = [EX_BASE + m.get("href") for m in matches]

    ex_data = {}
    for m in matches:
        e = m.split("/")[-1]
        p = getExchangePairs(m)
        ex_data[e] = p
        if "cccgen" in data.config.VERBOSE or "all" in data.config.VERBOSE:
            print()
            print(e)
            print(p)
        else:
            print('.', end='')
            sys.stdout.flush()

    print()

    return ex_data


def process(data):

    print("-----------------")
    print("| PAIRGEN_MODULE |")
    print("-----------------")

    exs = getExchanges(data)
    e_keys = exs.keys()
    for site in data.sites:
        if "cgen" in site:
            s_key = site['cgen']
            if s_key in e_keys:
                e_keys.remove(s_key)
                new_keys = exs[s_key]
                if len(new_keys) > 0:
                    site['tags'].extend(new_keys)
                else:
                    print("WARNING: no trading pairs for", s_key)
            else:
                print("WARNING: unmatched site key", s_key)
    for e in e_keys:
        print("WARNING: unused exchange key", e)





