CloudSkills = ["AWS", "Terraform", "Docker"]
TechincalSkills = ["Boto3", "OPA" , "DevOps", "Bash"]
GRCskills = ["ISO27001", "GDPR", "SOC", "HIPAA", "NIST"]

# To access by index, starting from zero
print(GRCskills[0]) # = ISO27001

# Slicing : To get a sub-section
print(GRCskills[1:4]) # ['GDPR', 'SOC', 'HIPAA']

# Append : To Add an Item to the very end
GRCskills.append("CIS")
print(GRCskills[5])

# Insert : To Add item at specific Index
GRCskills.insert(5, "PCI-DSS")
print(GRCskills)

# Remove : To remove the FIRST occurrence of a specific VALUE
GRCskills.remove("GDPR")
print(f"Removed GDPR from {GRCskills}") # GDPR is gone

# Pop : To remove and RETURN an item at a specific INDEX
# If no index is given, it pops the last item
last_skill = GRCskills.pop() # Removes "CIS" and stores it in last_skill
print(f"Popped item: {last_skill}")
print(GRCskills)

# Pop by index
second_skill = GRCskills.pop(1) # Removes the item at index 1 (SOC)
print(f"Popped second item: {second_skill}")
print(GRCskills)
 
# Length : Returns Numbers of items
total = len(GRCskills)
print(total)