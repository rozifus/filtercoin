#!/usr/bin/env python

from __future__ import print_function
import sys, os


def buildModelPairs(data, pairs):
    for pair in pairs.keys():
        pass

def getDominance(data):

    print(":GET_PAIR_DOMINANCE")

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
            print("WARNING: no order for both halves of pair", a, b)
            if a < b:
                return b,a
            else:
                return a,b
        else:
            print("WARNING: no order for half pair", a)
            return a,b
    elif b not in dom.keys():
        print("WARNING: no order for half pair", b)
        return b,a
    else:
        if dom[b] > dom[a]:
            return a,b
        else:
            return b,a

def process(data):

    print("----------------")
    print("| PAIRS_MODULE |")
    print("----------------")

    print(":NORMALIZE_PAIR_DOMINANCE")

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

    print(":BUILD_MODEL_PAIRS")

    buildModelPairs(data, pairs)




