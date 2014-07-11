from __future__ import print_function
import sys

RESET = '\033[0m'
WARNING = '\033[93m'
MAJOR = '\033[94m'
FINISHED = '\033[92m'

INCREMENTS = 30

def set_color(color):
    print(color, end="")

class Status:

    def __init__(self, mod_id="NO_ID", data=None):
        self.connect_data(data)
        self.mod_id = mod_id
        self.inc_step = 1
        self.inc_count = 0

    def set_mod_id(self, mod_id):
        self.mod_id = mod_id

    def connect_data(self, data):
        self.data = data

    def begin_module(self, name=None):
        if name == None:
            name = self.mod_id
        self.task(name)
    module = begin_module

    def task(self, task="UNNAMED_TASK"):
        set_color(MAJOR)
        print("# " + task.upper())
        set_color(RESET)
        #print("----" + "-" * len(task))
        #print("| " + task.upper() + " |")
        #print("----" + "-" * len(task))

    def major(self, name="UNNAMED"):
        set_color(MAJOR)
        print("=" * (len(name) + 4))
        print("# " + name.upper() + " #")
        print("=" * (len(name) + 4))
        set_color(RESET)

    def end_point(self, text="NO TEXT"):
        set_color(MAJOR)
        print("# " + text.upper() + " #")
        set_color(RESET)

    def warning(self, *args):
        set_color(WARNING)
        print("!", *args)
        set_color(RESET)
    warn = warning

    def verbose(self, *content):
        if self.is_verbose():
            print(*content)

    def begin_action(self, action):
        action = action.upper().replace(" ", "_")
        if action[0] != ": ":
            action = ": " + action
        print(action)
    action = begin_action

    def is_verbose(self):
        if self.data and (self.mod_id in self.data.config.VERBOSE or "all" in self.data.config.VERBOSE):
            return True
        return False


    def start_inc(self, col_size):
        self.inc_step = col_size / INCREMENTS
        if self.inc_step < 1:
            self.inc_step == 1
        self.inc_count = 0

    def inc(self, *inc):
        if self.is_verbose():
            for item in inc:
                print(item)
        else:
            self.inc_count += 1
            if self.inc_count % self.inc_step == 0:
                print(".",end="")
                sys.stdout.flush()

    def end_inc(self):
        self.inc_step = 1
        self.inc_count = 0
        print()

