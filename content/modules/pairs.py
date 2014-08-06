#!/usr/bin/env python

from __future__ import print_function
import sys, os
from modules.status import Status

status = Status("pairs")

def build_model_pair_components(data):

    status.action("BUILD_MODEL_PAIR_COMPS")

    masters = set([])
    model_components = []

    print("mp:",len(data.model_pairs))

    for pair in data.model_pairs:
        slave, master = pair.split("/")
        masters.add(master)

        mc = {}
        mc["par"] = "crypto/" + master
        mc["id"] = pair
        mc["name"] = pair.upper()
        mc["alias"] = ["/".join([master,slave])]

        model_components.append(mc)

    for master in masters:

        mc = {}
        mc["par"] = "pair"
        mc["id"] = "crypto/" + master
        mc["name"] = "Crypto/" + master.upper()
        mc["alias"] = master + "/crypto"

        model_components.append(mc)

    data.raw_model.extend(model_components)

    print("mc-count:", len(model_components), len(data.raw_model))

def generate_dominance(data):

    status.action("GEN_PAIR_DOMINANCE")

    dom = {}
    d = 1
    for c in reversed(data.order['crypto']):
        dom[c] = d
        d += 1
    for f in reversed(data.order['fiat']):
        dom[f] = d
        d += 1
    data.pair_dominance = dom

def dominantLast(a,b,data):
    dom = data.pair_dominance
    mip = data.missing_pairs
    if a not in dom.keys():
        if b not in dom.keys():
            if a not in mip or b not in mip:
                mip.add(a)
                mip.add(b)
                status.warn("no order for both halves of pair", a, b)
            if a < b:
                return b,a
            else:
                return a,b
        else:
            if a not in mip:
                mip.add(a)
                status.warn("no order for half pair", a)
            return a,b
    elif b not in dom.keys():
        if b not in mip:
            mip.add(b)
            status.warn("no order for half pair", b)
        return b,a
    else:
        if dom[b] > dom[a]:
            return a,b
        else:
            return b,a

def process(data):

    status.connect_data(data)
    generate_dominance(data)
    normalize_dominance(data)
    build_model_pair_components(data)

def normalize_dominance(data):
    status.action("NORMALIZE_PAIR_DOMINANCE")
    data.missing_pairs = set([])
    pairs = set([])
    for site in data.sites:
        tags = site['tags']
        for ti in range(len(tags)):
            if "/" in tags[ti]:
                a,b = tags[ti].split("/")
                new_tag = "/".join(dominantLast(a,b,data))
                pairs.add(new_tag)
                tags[ti] = new_tag

    data.model_pairs = pairs




