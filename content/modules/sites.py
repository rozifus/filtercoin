import json
import os
from modules.status import Status

def jsonFromFile(file_loc):
    with open(file_loc) as f:
        return json.load(f)
    return None

def jsonToFile(obj, file_loc):
    with open(file_loc, 'w') as f:
        json.dump(obj, f)

def getSites(site_dir):
    f_list = []
    for path,folders,files in os.walk(site_dir):
        f_list.extend([path+os.sep+f for f in files])

    sites = []
    for f_loc in f_list:
        sites.append(jsonFromFile(f_loc))

    return sites

def getModelComponents(site_dir):
    f_list = []
    for path,folders,files in os.walk(site_dir):
        f_list.extend([path+os.sep+f for f in files])

    subs = []
    for f_loc in f_list:
        subs.append(jsonFromFile(f_loc))

    return subs

def getModel(site_dir):
    comps = getModelComponents(site_dir)
    return buildModel(comps)

def buildModel(subs):
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


def getData(data):
    status = Status("READ_RAW_DATA")

    status.begin_action("GET_SITES")
    data.sites = getSites(data.config.SITES_INPUT_DIR)
    status.begin_action("GET_MODEL")
    data.model = getModel(data.config.MODEL_INPUT_DIR)
    status.begin_action("GET_ORDER")
    data.order = jsonFromFile(data.config.ORDER_INPUT)

def writeData(data):
    status = Status("WRITE_DATA")

    status.begin_action("WRITE_SITES")
    jsonToFile(data.sites, data.config.SITES_OUTPUT)
    status.begin_action("WRITE_MODEL")
    jsonToFile(data.model, data.config.MODEL_OUTPUT)


