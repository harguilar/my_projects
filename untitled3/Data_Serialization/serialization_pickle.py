import pickle
friends = {"Dan":[20, "London", 32], "maria": [25, "Madrid", 234]}

with open("friends.dat","wb") as f:
    pickle.dump(friends, f)

with open('friends.dat', "rb") as f:
    obj = pickle.load(f)
    print(obj)