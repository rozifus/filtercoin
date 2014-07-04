#!/usr/bin/env python

from __future__ import print_function
import sys, os
import urllib
from lxml.html import parse
from modules.status import Status


EX_BASE = "http://www.cryptocoincharts.info"
EX_LIST = EX_BASE + "/v2/markets/info"
EX_SHOW = EX_BASE + "v2/markets/show/"

status = Status("cccgen")

def getExchanges(data):

    def getExchangePairs(info_page):

        raw = urllib.urlopen(info_page)
        doc = parse(raw).getroot()
        matches = doc.cssselect("table tbody tr td a")
        ex_pairs = [m.text_content() for m in matches[1:]]

        if ex_pairs and ex_pairs[0] == "Show logged in users..":
            ex_pairs = ex_pairs[1:]

        return ex_pairs

    status.begin_action("GET_EXCHANGES")

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
        status.inc("",e,p)

    status.end_inc()

    return ex_data


def process(data):

    status.connect_data(data)

    exs = getExchanges(data)
    e_keys = exs.keys()
    for site in data.sites:
        if "auto" in site and site["auto"].startswith(":"):
            s_key = site['auto'][1:]
            if s_key in e_keys:
                e_keys.remove(s_key)
                new_keys = exs[s_key]
                if len(new_keys) > 0:
                    site['tags'].extend([nk.lower() for nk in new_keys])
                else:
                    status.warn("no trading pairs for", s_key)
            else:
                status.warn("unmatched site key", s_key)
    for e in e_keys:
        status.warn("unused exchange key", e)





