import os,sys
import modules.readwrite as rw
import modules.pop, modules.compress, modules.auto
import config

def getFiles(input_dir):
    result = []
    for path,folders,files in os.walk(input_dir):
        result.extend([path+os.sep+f for f in files])
    return result

if __name__ == "__main__":

    files = getFiles(config.SITES_INPUT_DIR)
    items = []
    for f_loc in files:
        item = rw.jsonFromFile(f_loc)
        if "item" in item:
            item = item["item"]
        items.append(item)
    print(len(items))

    #modules.pop.process(items)
    modules.auto.process(items)
    modules.pop.process(items)
    modules.compress.process(items)
    rw.jsonToFile(items, config.SITES_OUTPUT)

    model = rw.jsonFromFile(config.MODEL_INPUT)
    modules.compress.process(model)
    rw.jsonToFile(model, config.MODEL_OUTPUT)


