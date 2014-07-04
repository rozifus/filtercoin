import json
import os
from modules.status import Status

status = Status("MODEL")

def construct_tree(subs):
    status.action("BUILD_TREE")
    root = None
    for sub in subs[:]:
        if not "par" in sub:
            if root != None:
                print("ERROR: multiple roots in model")
                print(root)
                print(sub)
                exit()
            else:
                root = sub
                subs.remove(root)

    def get_matching_node(node, par):
        if node["id"] == par:
            return node
        elif "sub" in node:
            for s in node["sub"]:
                found = get_matching_node(s, par)
                if found:
                    return found
        return None

    s_count = len(subs) + 1
    while len(subs) < s_count:
        s_count = len(subs)
        for sub in subs[:]:
            target = get_matching_node(root, sub["par"])
            if target:
                sub.pop("par")
                target.setdefault("sub", []).append(sub)
                subs.remove(sub)
    if subs:
        print("ERROR: model failed to build!")
        exit()

    return root

def build(data):
    data.model = construct_tree(data.raw_model)

