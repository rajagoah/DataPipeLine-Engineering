import singer as sg
import json

candidate ={
                "firstName": "Jane",
                "lastName": "Doe",
                "hobbies": ["running", "sky diving", "singing"],
                "age": 35,
                "children": [
                    {
                        "firstName": "Alice",
                        "age": 6
                    },
                    {
                        "firstName": "Bob",
                        "age": 8
                    }
                ]
            }

#creating a schema
json_schema = {"properties":
                   {
                    "firstName" : {"type":"string"},
                    "lastName"  : {"type":"string"},
                    "hobbies"   : {"type":[]},
                    "age"       : {"type":"integer"},
                    "children"  : {"type":[]}
                   }
               }

#write_schema() function call
sg.write_schema(stream_name= 'candidate_stream', schema=json_schema, key_properties=[])

#write_records() function call
sg.write_record(stream_name= 'candidate_stream', record= candidate)

#using json.dumps() function
json_string = json.dumps(json_schema)
print("the serialised string version of the JSON is: \n", json_string)

#using the indent keyword argument makes the json more readable when outputing the result to console
json_string = json.dumps(json_schema, indent=2)
print("the serialised string version with indent is: \n", json_string)

#using json.dump() function
with open("data_file.json", "w") as write_file:
    json.dump(json_schema, write_file)

#using json.dump() function with the indent keyword
with open("data_file.json","w") as write_file:
    json.dump(json_schema, write_file, indent=4)