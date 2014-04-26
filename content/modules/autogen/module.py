#!/usr/bin/env python

from __future__ import print_function
import sys, os


def process(sites):
    for site in sites:
        if "auto" in site:
            path = "modules.autogen." + site["auto"]
            gen = None
            gen = __import__(path, fromlist=["autogen"])
            gen.autogen(site)
            del site["auto"]




