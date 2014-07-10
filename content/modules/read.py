import json
import os
from modules.status import Status

def jsonFromFile(file_loc):
    with open(file_loc) as f:
        return json.load(f)
    return None

def apply_all_file(af, target):
    for k,v in af.items():
        if k not in target:
            target[k] = v

def read_json_files(dir_head):
    result = []
    for path,folders,files in os.walk(dir_head):
        af_loc = path+os.sep+"__all.json"
        af = {}
        if os.path.isfile(af_loc):
            af = jsonFromFile(af_loc)
        for f in files:
            if not f.startswith("__"):
                j = jsonFromFile(path+os.sep+f)
                apply_all_file(af, j)
                result.append(j)

    return result


def read_json_file(dir_head):
    f_list = []
    for path,folders,files in os.walk(dir_head):
        f_list.extend([path+os.sep+f for f in files])

    result = []
    for f_loc in f_list:
        result.append(jsonFromFile(f_loc))

    return result

def process(data):
    status = Status("READ_DATA")

    status.begin_action("GET_SITES")
    data.sites = read_json_files(data.config.SITES_INPUT_DIR)
    status.begin_action("GET_MODEL")
    data.raw_model = read_json_files(data.config.MODEL_INPUT_DIR)
    status.begin_action("GET_ORDER")
    data.order = jsonFromFile(data.config.ORDER_INPUT)

