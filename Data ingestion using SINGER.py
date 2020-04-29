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

#exploring the data types of the variables declared above
#note that since the below variable is a set data type, we must remember that we cant slice a set.
#when we use the next() operator along with iter() operator on the users, the elements will be output
#in random order since the set is not an ordered collection. so everytime we run the below code, the
# output will vary for the users variables
print("users is: ", type(users))
print("accessing all elements of set by simply calling the name of the variable", next(iter(users)))

print("cols is: ", type(cols))
print("accessing all element of tuple using list's index notation", cols[0:3])

print("json is: ", type(json))

#--
#--

# Complete the JSON schema
schema = {'properties': {
                    'items' : {
                                'brand'         : {'type': 'string'},
                                'model'         : {'type': 'string'},
                                'price'         : {'type': 'number'},
                                'currency'      : {'type': 'string'},
                                'quantity'      : {'type': 'integer', 'minimum': 1},
                                'date'          : {'type': 'string', 'format': 'date'},
                                'countrycode'   : {'type': 'string', 'pattern': "^[A-Z]{2}$"},
                                'store_name'    : {'type': 'string'}
                                }
                        }
        }

# Write the schema
sg.write_schema(stream_name='products', schema=schema, key_properties=[])
print('writing done')