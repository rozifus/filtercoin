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

    """
    status.task("read files")
    read.get_data(data)

    status.task("cccgen")
    cccgen.process(data)

    status.task("pairs")
    pairs.process(data)

    status.task("build model")
    model.process(data)

    status.task("consistency")
    consistency.process(data)

    status.task("pop")
    pop.process(data)

    status.task("clean")
    clean.process(data)

    status.task("compress")
    compress.process(data)

    status.task("write site")
    write.write_data(data)
    """


