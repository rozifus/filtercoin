#!/usr/bin/env python

from __future__ import print_function
import sys, os


def process(sites):
    for site in sites:
        if "auto" in site:
            print("!auto!: ", site["auto"])
            del site["auto"]




