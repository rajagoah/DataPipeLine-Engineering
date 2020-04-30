import singer as sg

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
