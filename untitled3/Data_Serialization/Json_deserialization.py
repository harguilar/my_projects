import json

with open("Friends.json", "rt") as f:
    obj = json.load(f)
    print(type(obj))
    print(obj)