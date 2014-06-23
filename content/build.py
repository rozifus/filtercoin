import os,sys
import modules.readwrite as rw
from modules.status import Status
import config

if __name__ == "__main__":

    status = Status()

    class Data(object):
        pass

    data = Data()
    data.config = config

    rw.getData(data)

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

    rw.writeData(data)



