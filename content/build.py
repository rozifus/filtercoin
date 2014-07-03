import os,sys
import config
from modules import *

if __name__ == "__main__":

    status = Status()

    status.major("BUILD FILTERCOIN")

    class Data(object):
        pass

    data = Data()
    data.config = config

    status.task("read files")
    read.get_data(data)

    status.task("cccgen")
    cccgen.process(data)

    status.task("pairs")
    pairs.process(data)

    status.task("build model")
    model.build(data)

    status.task("consistency")
    consistency.process(data)

    status.task("pop")
    pop.process(data)

    status.task("compress")
    compress.process(data)

    status.task("write site")
    write.write_data(data)


    status.major("FILTERCOIN BUILT!")

