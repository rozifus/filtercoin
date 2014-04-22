#!/usr/bin/env python

from __future__ import print_function
import sys, os


def process(sites):
    for site in sites:
        if "auto" in site:
            path = "modules.autogen." + site["auto"]
            gen = None
            try:
                print(path)
                gen = __import__(path, fromlist=["autogen"])
                print(dir(gen))
                gen.autogen()
            except:
                print("!autogen module problem!: ", gen_loc)
            finally:
                del site["auto"]




