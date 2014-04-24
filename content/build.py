import os,sys
import modules.readwrite as rw
import modules.consistency, modules.pairs
import modules.pop, modules.compress, modules.autogen
import config

def getFiles(input_dir):
    result = []
    for path,folders,files in os.walk(input_dir):
        result.extend([path+os.sep+f for f in files])
    return result

if __name__ == "__main__":

    files = getFiles(config.SITES_INPUT_DIR)
    model = rw.jsonFromFile(config.MODEL_INPUT)
    order = rw.jsonFromFile(config.ORDER_INPUT)

    items = []
    for f_loc in files:
        item = rw.jsonFromFile(f_loc)
        if "item" in item:
            item = item["item"]
        items.append(item)
    print(len(items))

    modules.autogen.process(items)
    modules.pairs.process(items)
    modules.consistency.process(model, items, order)
    #modules.pop.process(items)
    modules.compress.process(items)
    rw.jsonToFile(items, config.SITES_OUTPUT)

    modules.compress.process(model)
    rw.jsonToFile(model, config.MODEL_OUTPUT)


