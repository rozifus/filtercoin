import json

def jsonFromFile(file_loc):
    with open(file_loc) as f:
        print(f)
        return json.load(f)
    return None

def jsonToFile(obj, file_loc):
    with open(file_loc, 'w') as f:
        json.dump(obj, f)


