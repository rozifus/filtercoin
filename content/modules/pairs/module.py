#!/usr/bin/env python

from __future__ import print_function
import sys, os
from modules.status import Status

status = Status("pairs")

def buildModelPairs(data):

    model_pair_tree = {"crypto/fiat": {}, "crypto/crypto": {}}

    for pair in data.model_pairs.keys():
        slave, master = pair.split("/")
        if master in data.order['fiat']:
            if model_pair_tree():
                pass


def getDominance(data):

    status.begin_action("GET_PAIR_DOMINANCE")

    dom = {}
    d = 1
    for c in reversed(data.order['crypto']):
        dom[c] = d
        d += 1
    for f in reversed(data.order['fiat']):
        dom[f] = d
        d += 1
    return dom

def dominantLast(a,b,dom):
    if a not in dom.keys():
        if b not in dom.keys():
            status.warn("no order for both halves of pair", a, b)
            if a < b:
                return b,a
            else:
                return a,b
        else:
            status.warn("no order for half pair", a)
            return a,b
    elif b not in dom.keys():
        status.warn("no order for half pair", b)
        return b,a
    else:
        if dom[b] > dom[a]:
            return a,b
        else:
            return b,a

def process(data):

    status.connect_data(data)
    status.begin_action("NORMALIZE_PAIR_DOMINANCE")

    dom = getDominance(data)
    pairs = {}
    for site in data.sites:
        tags = site['tags']
        for ti in range(len(tags)):
            if "/" in tags[ti]:
                a,b = tags[ti].split("/")
                new_tag = "/".join(dominantLast(a,b,dom))
                pairs[new_tag] = True
                tags[ti] = new_tag

    status.begin_action("BUILD_MODEL_PAIRS")

    data.model_pairs = pairs
    buildModelPairs(data)




