#!/usr/bin/env python

from __future__ import print_function
import sys, os
from modules.status import Status

status = Status("compress")

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
            rcopy = root.copy()
            compress(v)
            del root[k]
            if k not in COMP.keys():
                status.warn("unknown uncompressed key '{0}'".format(k))
                status.verbose(rcopy)
                print(rcopy)
            else:
                root[COMP[k]] = v

def process(data):
    status.action("compress_sites")
    compress(data.sites)
    status.action("compress_model")
    compress(data.model)




