#!/usr/bin/env python

from __future__ import print_function
import sys, os
from modules.status import Status


status = Status("implies")

def pairs_implies_singles(data):

    status.action("pairs implies singles")

    for site in data.sites:
        tag_set = set()
        for t in site['tags']:
            tag_set.add(t)
            if "/" in t:
                tag_set.update(t.split("/"))
        site['tags'] = list(tag_set)

def process(data):

    status.connect_data(data)

    pairs_implies_singles(data)




