### MERGING JSONS USING THE MERGE PACKAGE. THIS IS MORE INTUTIVE BUT MAY NOT BE VERY EFFICIENT
#importing appropriate packages
import json
from jsonmerge import merge
import glob

json1 = {"comments":"this is a comment"}

json2 = {"body":"this is the body of the json"}

json_merge = {}

json_merge = merge(json1, json2)

print(json_merge)

with open("data_file_merge.json", "w") as wf:
    json.dump(json_merge, wf, indent=4, separators=(", " , ": "))

### USING THE NON PACKAGE METHOD TO MERGE JSONS
#use the load() function to deserialize the JSON
result = []
for file in glob.glob("*.json"):
    with open(file, "r") as infile:
        result.append(json.load(infile))

with open("data_file_merged_2.json","w") as outfile:
    json.dump(result, outfile)