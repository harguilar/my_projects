import json
#Define a Dictionary Friends which is a python object
friends = { "Dan": [22, "London", 4443343], "Maria":[25, "Madrid", 55566445]}
#Create a File Friends
with open ("Friends.json", "w") as f:
    #Write a Json File indent 4 is use 4 spaces for indentation
    json.dump(friends, f, indent=4)

#Create a STRING representation of Python Object in Jason Representation
json_string = json.dumps(friends)
print(json_string)


Friends = { "Harguilar":[35, "Avenida Comandante Valodia", 236], "Jessica":[28, "Avenida Comandante Valodia", 236],
            "Jeila":[1, "Avendia Comandante Valodia", 236]
}
with open("Friends.json", "w") as File:
    json.dump(Friends,File, indent=4)
