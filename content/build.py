import os,sys
import config
from modules.status import Status

if __name__ == "__main__":

    status = Status()

    class Data(object):
        pass

    data = Data()
    data.config = config

    status.major("BUILD " + config.NAME)

    active_modules = [
        "read",
        "cccgen",
        "normalize",
        "pairs",
        "implies",
        "model",
        "consistency",
        "pop",
        "clean",
        "compress",
        "write"
    ]

    for am in active_modules:
        status.task(am)
        module_path = "modules." + am
        module = __import__(module_path, fromlist=["process"])
        module.process(data)

    status.major(config.NAME + " BUILT!")



