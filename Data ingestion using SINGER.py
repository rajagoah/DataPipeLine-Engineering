#importing package to create a JSON
import singer as sg

cols = ("id","name","age")

users = {(1,"ar",32),
         (2,"sr",31),
         (3,"rr",33 )}
json = {"properties" :
            {
                "id" : {"type":"integer"},
                "name" : {"type":"string"},
                "age"  : {"type":"integer"}
            }
        }

#the write schema method converts the above JSON into a schema
sg.write_schema(stream_name="user_stream",schema=json, key_properties = ["id"])