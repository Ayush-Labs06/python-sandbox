# Python has inbuilt module 'json' for basic works
import json

user = {
    "name" : "Ayush",
    "role" : "Auditor",
    "adult" : True
}

# json.dumps(dict) -> Python dict to JSON string
# json.loads(string) -> JSON string to Python dict

json_data = json.dumps(user, indent=4)

with open("json_yaml/user.json", "w") as f:
    f.write(json_data)
print(json_data)


# To convert JSON string to Python dict, the input must be a string.
Info = '{"name": "ayush", "age": 19, "active": true}'

BioData = json.loads(Info)

print(BioData["age"])


# Reading JSON from a file

with open("json_yaml/certs.json", "r") as f:
    certs = json.load(f)
    
    print(certs)