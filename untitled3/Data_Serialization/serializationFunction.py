import json

#Serialization
def serialization(obj, file, prot):

    if prot == 'pickle':
        import pickle
        with open(file, 'wb') as f:
           pickle.dumps(obj,f)
    elif prot == 'json':
        import json
        with open(file, 'w') as f:
            json.dump(obj,f)
    else:
        print ("Invalid Serialization Usage: Use Pickle or Json")

#Deserializing
def deserialize(file, prot):
    if prot == "pickle":
        import pickle
        with open(file, 'wb') as f:
            obj = pickle.load(f)
        return obj

    elif prot == "json":
        import json
        with open(file, 'r') as f:
            obj = json.dump(f)
        return obj
    else:
        print ("Invalid Information Provided. It has to be Pickle or Json")


if __name__ == "__main__":
    d1 = {'a': 'x', 'b': 'y', 'c': 'z', 30: (2, 3, 'a')}

    # Serializing using pickle
    serialization(d1, 'a.dat', 'pickle')

    # Deserializing
    myDict = deserialize('a.dat', 'pickle')
    print(f'pickle: {myDict}')

    print('#' * 20)

    # serializing using pickle
    serialization(d1, 'a.json', 'json')

    # deserializing
    x = deserialize('a.json', 'json')
    # Notice how the tuple value was not preserved!
    print(f'json: {x}')  # {'a': 'x', 'b': 'y', 'c': 'z', '30': [2, 3, 'a']}


