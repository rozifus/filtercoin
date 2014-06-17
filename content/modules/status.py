from __future__ import print_function


def begin_module(name):
    print("-" * 2 + "-" * len(name) + "-" * 9)
    print("| " + name.upper() + "_MODULE |")
    print("-" * 2 + "-" * len(name) + "-" * 9)

def warning(*args):
    print("WARNING: ", *args)
warn = warning

def begin_action(action):
    action = action.upper().replace(" ", "_")
    if action[0] != ":":
        action = ":" + action
    print(action)

def inc():
    print(".",end="")

def end_inc():
    print()

