#!/usr/bin/env python

from __future__ import print_function
import sys, os

EXP = {
    "h": "href",
    "t": "tags",

    "n": "name",

    "i": "id",
    "a": "alias",
    "p": "pop",
    "s": "sub",
}
COMP = {}
for k,v in EXP.iteritems():
    COMP[v] = k

def compress(root):
    if type(root) == type([]):
        for item in root:
            compress(item)
    elif type(root) == type({}):
        for k,v in root.items():
            compress(v)
            del root[k]
            root[COMP[k]] = v

def process(data):
    compress(data)




