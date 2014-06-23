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

def getModel(config):
    f_list = []
    for path,folders,files in os.walk(site_dir):
        f_list.extend([path+os.sep+f for f in files])

    subs = []
    for f_loc in f_list:
        subs.append(jsonFromFile(f_loc))

    ps = len(subs) + 1
    while len(subs) > 1:
        if len(subs) == ps:
            print("ERROR: Model failed to build!")
            for sub in subs:
                print(sub)
            exit()



def getData(data):
    status = Status("READ_RAW_DATA")
    status.begin_module()

    status.begin_action("GET_SITES")
    data.sites = getSites(data.config.SITES_INPUT_DIR)
    status.begin_action("GET_MODEL")
    data.model = jsonFromFile(data.config.MODEL_INPUT)
    status.begin_action("GET_ORDER")
    data.order = jsonFromFile(data.config.ORDER_INPUT)

def writeData(data):
    status = Status("WRITE_DATA")
    status.begin_module()

    status.begin_action("WRITE_SITES")
    jsonToFile(data.sites, data.config.SITES_OUTPUT)
    status.begin_action("WRITE_MODEL")
    jsonToFile(data.model, data.config.MODEL_OUTPUT)


