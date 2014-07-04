import json
import os
from modules.status import Status

def jsonFromFile(file_loc):
    with open(file_loc) as f:
        return json.load(f)
    return None

def read_json_files(dir_head):
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

