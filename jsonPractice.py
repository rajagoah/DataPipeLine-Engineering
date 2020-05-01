import json

#json variable
json1 = {"comment":"hello, this is a comment"}

#serializing a json
with open("data_file.json","w") as write_file:
    json.dump(json1, write_file)

#deserializing a json
with open("data_file.json","r") as read_file:
    data = json.load(read_file)
print(data)

