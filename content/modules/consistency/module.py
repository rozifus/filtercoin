#!/usr/bin/env python

from __future__ import print_function
import sys, os
from modules.status import Status

status = Status("consistency")

def unique_dict_add(val, d):
    if val in d:
        status.warn("duplicate value '{0}'".format(val))
        status.verbose(d)
    else: d[val] = True

def collect_node_tags(node, found):
    ident = node["id"]
    unique_dict_add(ident, found)
    if "sub" in node:
        for d in node["sub"]:
            collect_node_tags(d, found)

collect_model_tags = collect_node_tags

def collect_item_tags(items, found):
    for item in items:
        if "tags" in item:
            for tag in item["tags"]:
                found[tag] = True

def collect_order_tags(order, found):
    fiat_list = order["fiat"]
    crypto_list = order["crypto"]

    for tag in fiat_list:
        unique_dict_add(tag, found)
    for tag in crypto_list:
        unique_dict_add(tag, found)


def process(data):
    dModel = {}
    dItems = {}
    dOrder = {}

    status.action("collect_model_tags")
    collect_model_tags(data.model, dModel)

    status.action("collect_item_tags")
    collect_item_tags(data.sites, dItems)

    status.action("collect_order_tags")
    collect_order_tags(data.order, dOrder)


