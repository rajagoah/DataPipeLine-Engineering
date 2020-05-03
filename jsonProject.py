import json
import requests

#the request variable now contains the contents of the todos end point in the form of a json
request = requests.get("https://jsonplaceholder.typicode.com/todos")

#the todos varaible will contain the content in the request variable in the form of a list
todos = json.loads(request.text)

#calculating the number of user id that have completed the task.
# For this we have to increment the counter by 1 everytime, we see completed = True
dic = {}
cntr = 0
user_cnts_dic = {}
for i in todos:
    dic = i

    if dic["completed"] == True:
        user_cnts_dic.setdefault(dic["userId"],0)
        user_cnts_dic[dic["userId"]] = user_cnts_dic[dic["userId"]] + 1
    else:
        continue
print(user_cnts_dic)

#now finding out the user id that have the max count

max_v   = 0  #to hold the value of the value at that instance in the iteration
prev_v  = 0
key     = []      #to hold the value of the key at that instance in the iteration. This value of the Key will correspond the value being iterated over.
for k,v in user_cnts_dic.items():
    if int(v) >= max_v:
        max_v  = int(v)
        key.append(k)
    else:
        continue

#logic to remove the [1] from the key list created above.
# If you study the keys copied in to the key list, you will notice that [1] is the incorrect entry
max_v   = user_cnts_dic[key[1]]
prev_v  = 0
key.reverse()
for i in key:
    if user_cnts_dic[i] >= max_v:
        max_v = user_cnts_dic[i]
        continue
    else:
        key.remove(i)

print("the user having completed the most tasks is: ", key)





