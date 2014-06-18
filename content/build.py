import os,sys
import modules.readwrite as rw
import modules.consistency, modules.pairs
import modules.pop, modules.compress, modules.autogen
import modules.cccgen, modules.normalize
from modules.status import Status
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

    status = Status()

    class Data(object):
        pass
    data = Data()

    data.config = config
    data.sites = getSites(config.SITES_INPUT_DIR)
    data.model = rw.jsonFromFile(config.MODEL_INPUT)
    data.order = rw.jsonFromFile(config.ORDER_INPUT)

    active_modules = [
        "cccgen",
        #"autogen",
        "normalize",
        "pairs",
        "consistency",
        "pop",
        "compress"
    ]

    for am in active_modules:
        status.begin_module(am)
        module_path = "modules." + am
        module = __import__(module_path, fromlist=["process"])
        module.process(data)

    """
    # run modules
    modules.cccgen.process(data)
    #modules.autogen.process(data)
    modules.normalize.process(data)
    modules.pairs.process(data)
    modules.consistency.process(data)
    modules.pop.process(data)
    modules.compress.process(data)
    """

    print("--------------")
    print("| WRITE_DATA |")
    print("--------------")
    print(":WRITE_SITES")
    rw.jsonToFile(data.sites, config.SITES_OUTPUT)
    print(":WRITE_MODEL")
    rw.jsonToFile(data.model, config.MODEL_OUTPUT)



