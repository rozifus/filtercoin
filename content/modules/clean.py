#!/usr/bin/env python

from __future__ import print_function
import sys, os
from modules.status import Status

status = Status("clean")

PURGE = ["auto"]

def process(data):
    status.action("data.sites has 'dead'")
    print(len(data.sites))
    data.sites = [s for s in data.sites if ("dead" not in s)]
    print(len(data.sites))

    for p in PURGE:
        status.action("sites|" + p)
        for site in data.sites:
            if p in site.keys():
                del(site[p])






