import json
import os
from modules.status import Status

def jsonToFile(obj, file_loc):
    with open(file_loc, 'w') as f:
        json.dump(obj, f)

def process(data):
    status = Status("WRITE_DATA")

    status.begin_action("WRITE_SITES")
    jsonToFile(data.sites, data.config.SITES_OUTPUT)
    status.begin_action("WRITE_MODEL")
    jsonToFile(data.model, data.config.MODEL_OUTPUT)


