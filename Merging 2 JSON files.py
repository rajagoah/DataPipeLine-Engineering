### MERGING JSONS USING THE MERGE PACKAGE. THIS IS MORE INTUTIVE BUT MAY NOT BE VERY EFFICIENT
#importing appropriate packages
import json
from jsonmerge import merge

json1 = {"comments":"this is a comment"}

json2 = {"body":"this is the body of the json"}

json_merge = {}

json_merge = merge(json1, json2)

print(json_merge)

with open("data_file_merge.json", "w") as wf:
    json.dump(json_merge, wf, indent=4, separators=(", " , ": "))