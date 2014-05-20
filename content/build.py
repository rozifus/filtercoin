import os,sys
import modules.readwrite as rw
import modules.consistency, modules.pairs
import modules.pop, modules.compress, modules.autogen
import modules.cccgen
import config

def getSites(site_dir):
    f_list = []
    for path,folders,files in os.walk(site_dir):
        f_list.extend([path+os.sep+f for f in files])

    sites = []
    for f_loc in f_list:
        sites.append(rw.jsonFromFile(f_loc))

    return sites

if __name__ == "__main__":

    class Data(object):
        pass
    data = Data()

    print(config.SITES_INPUT_DIR)

    data.config = config
    data.sites = getSites(config.SITES_INPUT_DIR)
    data.model = rw.jsonFromFile(config.MODEL_INPUT)
    data.order = rw.jsonFromFile(config.ORDER_INPUT)

    #sites
    modules.cccgen.process(data)
    #modules.autogen.process(data)
    modules.pairs.process(data)
    modules.consistency.process(data)
    modules.pop.process(data)
    modules.compress.process(data)
    rw.jsonToFile(data, config.SITES_OUTPUT)

    #model
    modules.compress.process(model)
    rw.jsonToFile(model, config.MODEL_OUTPUT)


