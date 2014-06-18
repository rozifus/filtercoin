from __future__ import print_function
import sys

class Status:
    def __init__(self, mod_id="NO_ID", data=None):
        self.connect_data(data)
        self.mod_id = mod_id

    def set_mod_id(self, mod_id):
        self.mod_id = mod_id

    def connect_data(self, data):
        self.data = data

    def begin_module(self, name=None):
        if name == None:
            name = self.mod_id
        print("-" * 2 + "-" * len(name) + "-" * 9)
        print("| " + name.upper() + "_MODULE |")
        print("-" * 2 + "-" * len(name) + "-" * 9)
    module = begin_module

    def warning(self, *args):
        print("WARNING: ", *args)
    warn = warning

    def begin_action(self, action):
        action = action.upper().replace(" ", "_")
        if action[0] != ":":
            action = ":" + action
        print(action)
    action = begin_action

    def inc(self, *inc):
        if self.mod_id in self.data.config.VERBOSE or "all" in self.data.config.VERBOSE:
            for item in inc:
                print(item)
        else:
            print(".",end="")
            sys.stdout.flush()

    def end_inc(self):
        print()

