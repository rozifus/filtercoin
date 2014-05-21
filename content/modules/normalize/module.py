#!/usr/bin/env python

from __future__ import print_function
import sys, os



def normalizeTag(t):
    t = t.replace("\\","/").lower()
    return t

def process(data):
    for site in data.sites:
        site['tags'] = [normalizeTag(t) for t in site['tags']]




