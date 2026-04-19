# Dictionary ('dict') is collection of key-value pairs
# my_dict = {"id1" "value1", "id2": "value2"}

BioData = {
    "Name" : "Ayush",
    "Age" : 19,
    "skills" : ["cloud", "security", "GRC"]
}

print(BioData)

# Access (crashes if key doesn't exist)
print(BioData["Age"])

# Safe Access (if key doesnt exist, returns None or a default value)
# 1. Standard get (returns None if missing)
print(BioData.get("Location")) 

# 2. Get with default (returns "Not Found" if missing)
print(BioData.get("Location", "Not Found!"))

# 3. Successful get
print(BioData.get("Name"))


# Add / Update (If key doesnt exist, it adds. if exist, updates)
BioData["role"] = "TechincalGRC"
print(BioData)

# Delete 
del BioData["role"]
print(BioData)

# ----   ---- 

print(BioData.keys())

print(BioData.values())

print(BioData.items())

# Nested structure

first_skill = BioData["skills"][0]
print(first_skill)