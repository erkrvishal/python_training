# f = open("test.txt",'r',encoding='utf-8')
# print(f.read())
# for line in f:
#     print(line, end='')
#     break

# x = f.readlines()
# print(x[-1])

# with open("test.txt","w",encoding='utf-8') as file: # replaced a+ with w
#     file.write("My name is Vishal\n")
#     file.write("My name is Kumar\n")
#     file.write("Error\n")

import json
import boto3
# file_name.json
# dump and dumps = dump is used only with files, dumps --> converts JSON to JSON String
# load and loads = load is used only with files, loads --> Converts JSON String to JSON
temp = {
    "first_name": "Vishal",
    "last_name": "Kumar",
    "session": "Python"
}

# with open("test_1.json","w") as outfile:
#     json.dump(temp, outfile)

with open("test_1.json",'r') as file:
    json_output = json.load(file)
    print(json_output["last_name"])