#!/usr/bin/env python

from __future__ import print_function
import sys, os
from modules.status import Status

status = Status("clean")

PURGE = ["auto"]

def process(data):
    for p in PURGE:
        status.action("sites|" + p)
        for site in data.sites:
            if p in site.keys():
                del(site[p])






