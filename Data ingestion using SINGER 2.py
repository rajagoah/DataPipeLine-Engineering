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

#using the separators keyword argument in dump() function, to specify an alternate separator
#using ("," , ":") as separator
json_string = json.dumps(json_schema, indent=4, separators=(",",":"))
print("""the serialised string version with indent and separators as ("," , ":")is: \n""", json_string)

#using (", ", ": ") as separator
json_string = json.dumps(json_schema, indent= 4, separators= (", " , ": "))
print("""the serailised string version with indent and separator as  (", " , ": ") \n""", json_string )

#using json.dump() function
comment = {"comment" : " {************************THIS IS A DEMO OF json.dump() FUNCTION LOOKS LIKE************************}\n"}
with open("data_file.json", "w") as write_file:
    json.dump(comment, write_file)
    json.dump(json_schema, write_file)

#using json.dump() function with the indent keyword
comment = {"comment" : " {************************THIS IS A DEMO OF WHAT USING INDENT KEYWORD ARGUMENT LOOKS LIKE************************}\n"}
with open("data_file.json","w") as write_file:
    json.dump(comment, write_file)
    json.dump(json_schema, write_file, indent=4)

#using separtors key word with value as (", " , ": ")
comment = {"comment" : "{************************THIS IS A DEMO OF WHAT USING SEPARATORS = (", " , ": ") LOOKS LIKE************************}\n"}
with open("data_file.json","w") as write_file:
    json.dump(comment, write_file)
    json.dump(json_schema, write_file, indent= 4, separators= (", " , ": "))

#using the separtors key word with value s ("," , ":")
comment = {"comment" : """{************************THIS IS A DEMO OF WHAT USING SEPARATORS = ("," , ":") LOOKS LIKE************************}\n"""}
with open("data_file2.json","w") as write_file:
    json.dump(comment, write_file)
    json.dump(json_schema, write_file, indent= 4, separators = ("," , ":"))

