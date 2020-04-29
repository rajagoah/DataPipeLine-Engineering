#importing package to create a JSON
import singer as sg

########################################### PRACTICE CODE ###########################################
"""
#practicing the dict() constructor
nums = dict(x=1,y=2)
print(type(nums))
print(nums)

#creating a dictionary using iteratable
nums1 = dict([('x',5),('y',4)])
print(nums1)

nums2 = dict([('x',3),('y',6)],z=7)
print(nums2)

nums3 = list(zip(['x','y','z'],[1,3,5]))
print(nums3)
print(dict(nums3))

nums4 = dict(zip(['p','q','r'],[6,8,0]))
print(nums4)

qwe = ('q','t','z')
asd = {(1,2,3),(4,5,6),(7,8,9)}
print(asd.pop())
print(dict(zip(qwe,asd.pop())))

#understood the nuances of using pop() method with the zip() method. the difference in the way the two iterators get mapped.
#--the pop() method removes and outputs an elements from the set in random order.
# additionally, it maps each element in tuple <qwe> to each element enclosed in parenthesis within the set <asd>.
# Since the pop() method removes elements randomly, the q,t,z may get matched to any of the 3 elements of the set <asd>
cols = ("id","name","age")

#exploring the data types of the variables declared above
#note that since the below variable is a set data type, we must remember that we cant slice a set.
#when we use the next() operator along with iter() operator on the users, the elements will be output
#in random order since the set is not an ordered collection. so everytime we run the below code, the
# output will vary for the users variables
print("users is: ", type(users))
print("accessing all elements of set by simply calling the name of the variable", next(iter(users)))

print("cols is: ", type(cols))
print("accessing all element of tuple using list's index notation", cols[0:3])

print("json is: ", type(json))"""
########################################### PROJECT CODE ###########################################

#practing the use of singer package to create a tap

#creating a header that will serve as keys
cols = ['id','name','age']

#data to be popualted as records to the tap
users = {(1,"ar",32),
         (2,"sr",31),
         (3,"rr",33 )}

#schema that defines the structure of data storage
json = {"properties" :
            {
                "id" : {"type":"integer"},
                "name" : {"type":"string"},
                "age"  : {"type":"integer"}
            }
        }

#converting the users and cols to 1 combined dictionary
comb_dict = dict(zip(cols, users.pop()))
print("combined dictionary is: ", comb_dict)

#write_schema() function call
sg.write_schema(stream_name="user_stream",schema=json,key_properties=["id"])

#write_record() function call
sg.write_record(stream_name="user_stream",record=comb_dict)

#write_records() function call to map multiple records
sg.write_records(stream_name="user_srteam",records=comb_dict)



