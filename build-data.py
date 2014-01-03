import os,sys
import json

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



if __name__ == "__main__":

    INPUT_DIR = "./data"
    OUTPUT_DIR = "./www/data"
    OUTPUT_NAME = "data.json"

    files = getFiles(INPUT_DIR)
    items = []
    for f_loc in files:
        item = getJsonFromFile(f_loc)
        if "item" in item:
            item = item["item"]
        items.append(item)
    writeJsonToFile(items, OUTPUT_DIR + os.sep + OUTPUT_NAME)


