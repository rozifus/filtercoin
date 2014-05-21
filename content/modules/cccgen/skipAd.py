#!/usr/bin/env python

from __future__ import print_function
import sys, os
import urllib
from lxml.html import parse
import modules.readwrite as rw

from selenium import webdriver


EX_BASE = "http://www.cryptocoincharts.info"
EX_LIST = EX_BASE + "/v2/markets/info"
EX_SHOW = EX_BASE + "v2/markets/show/"

sys.path

def skipAd(adUrl):

    print(adUrl)
    options = webdriver.chrome.options.Options()
    options.add_argument("-incognito")
    mydriver = webdriver.Chrome(chrome_options=options)
    mydriver.get(adUrl)
    mydriver.maximize_window()

    """

    raw = urllib.urlopen(EX_LIST)
    doc = parse(raw).getroot()

    matches = []
    matches += doc.cssselect("#tableMarkets tbody tr td a")
    matches = [EX_BASE + m.get("href") for m in matches]

    for m in matches:
        getExchangeInfo(m)

    if "cccgen" in data.config.VERBOSE or "all" in data.config.VERBOSE:
        print("___CCCGEN:GET_EXCHANGES___")
        for m in matches:
            print(m)
        print("--------------------------")

    """

