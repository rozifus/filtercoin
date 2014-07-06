#!/usr/bin/env python

from __future__ import print_function
import sys, os

SCRAPERS = [
    "ccc"
]

def process(data):

    data.scraped = {}
    for scraper in SCRAPERS:
        status.action(scraper)
        path = "modules.scraper." + scraper
        gen = None
        gen = __import__(path, fromlist=["scrape"])
        if gen:
            gen.scrape(data.scraped)




