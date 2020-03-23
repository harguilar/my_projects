import json
import requests

response = requests.get("http://jsonplaceholder.typicode.com/todos")

if response.status_code == 200:
    # load Json encode strings into a python object
    pythonString = json.loads(response.text)

    print(type(pythonString))
    print(pythonString)

    for tasks in pythonString:
        if tasks['completed'] == True:
            print(tasks)
else:
    print ("You Have got an Error ")