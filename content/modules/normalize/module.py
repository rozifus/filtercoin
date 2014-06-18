#!/usr/bin/env python

from __future__ import print_function
import sys, os
from modules.status import Status

status = Status("normalize")

def normalizeTag(t):
    t = t.replace("\\","/").lower()
    return t

def process(data):
    status.action("normalize_site_tags")
    for site in data.sites:
        site['tags'] = [normalizeTag(t) for t in site['tags']]




