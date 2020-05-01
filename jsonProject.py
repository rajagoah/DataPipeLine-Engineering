import json
import requests

request = requests.get("https://jsonplaceholder.typicode.com/todos")

#the below command can also be done using the following code: todo = json.load(request.text)
todo = request.text
print("todo variable populated")

