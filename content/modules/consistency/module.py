#!/usr/bin/env python

from __future__ import print_function
import sys, os

def unique_dict_add(val, d):
    if val in d:
        print("Error duplicate value:", val)
    else: d[val] = True

def collect_node_tags(node, found):
    ident = node["id"]
    unique_dict_add(ident, found)
    if "sub" in node:
        for d in node["sub"]:
            collect_node_tags(d, found)

collect_model_tags = collect_node_tags

def collect_item_tags(items, found):
    print("items")
    for item in items:
        if "tags" in item:
            for tag in item["tags"]:
                found[tag] = True

def collect_order_tags(order, found):
    print("orders")
    fiat_list = order["fiat"]
    crypto_list = order["crypto"]

    for tag in fiat_list:
        unique_dict_add(tag, found)
    for tag in crypto_list:
        unique_dict_add(tag, found)


def process(inModel, inItems, inOrder):
    dModel = {}
    dItems = {}
    dOrder = {}

    collect_model_tags(inModel, dModel)
    collect_item_tags(inItems, dItems)
    collect_order_tags(inOrder, dOrder)


