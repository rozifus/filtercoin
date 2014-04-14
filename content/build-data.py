import os,sys
import json
from pop import getPop
import config

def getFiles(input_dir):
    result = []
    for path,folders,files in os.walk(input_dir):
        result.extend([path+os.sep+f for f in files])
    return result

def getJsonFromFile(file_loc):
    with open(file_loc) as f:
        print(f)
        return json.load(f)
    return None

def writeJsonToFile(obj, file_loc):
    with open(file_loc, 'w') as f:
        json.dump(obj, f)


def addPops(items):
    for item in items:
        item["pop"] = getPop(item["href"])

if __name__ == "__main__":

    files = getFiles(config.INPUT_DIR)
    items = []
    for f_loc in files:
        item = getJsonFromFile(f_loc)
        if "item" in item:
            item = item["item"]
        items.append(item)
    print(len(items))
    addPops(items)
    writeJsonToFile(items, config.OUTPUT_DIR + os.sep + config.OUTPUT_NAME)


