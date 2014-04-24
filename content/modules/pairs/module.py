#!/usr/bin/env python

from __future__ import print_function
import sys, os


def process(sites):
    for site in sites:
        if "pair" in site:
            del site["pair"]




