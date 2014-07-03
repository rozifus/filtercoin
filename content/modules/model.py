import json
import os
from modules.status import Status

def read_raw(site_dir):
    status.action("get components")
    f_list = []
    for path,folders,files in os.walk(site_dir):
        f_list.extend([path+os.sep+f for f in files])

    subs = []
    for f_loc in f_list:
        subs.append(jsonFromFile(f_loc))

    return subs

def build(subs):
    status.action("build model")
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
                target["sub"].append(sub)
                subs.remove(sub)
    if subs:
        print("ERROR: model failed to build!")
        exit()

    return root


def read_raw(site_dir):
    comps = getModelComponents(site_dir)
    return buildModel(comps)




