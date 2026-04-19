# Triple Nested Loops in Python
# Format: Counter : Name : Role

names = ["Ayus", "luke", "Witcher"]
roles = ["Solution Architect", "manager", "IsWitcher"]
seniorityDesignation = ["junior", "senior", "AuraFarmer"]
info = {"name": "Ayush", 
        "role": "SA", 
        "id": 1}


#  Iteration over a List
for name in names:
    print(f"User: {name}...")
    
    
for i in range(len(roles)):
    print(f"{i+1} : {roles[i]}")


# Using 'enumerate()' for formatted output
for i, role in enumerate(roles, start=1):
    print(f"{i} : {role}")
    
# Iteration over Dictionary
for key, value in info.items():
    print(f"{key}-{value}")
    
# use zip to iterate over two or more lists in parallel
for name,desig,role in zip(names,seniorityDesignation,roles):
    print(f"{name} is of {desig} clearance with {role} role")
    
# We can combine like
for i, (name, desig, role) in enumerate(zip(names, seniorityDesignation, roles), start=1):
    print(f"{i}. {name} is of {desig} clearance with {role} role")
    

# ex - Create a list of squares for even numer
numbers = range(10)
squares = [x**2 for x in numbers if x % 2 == 0]
print(squares) # [0, 4, 16, 36, 64]

# While Loops
# 'While' loops run as long as a condition remains 'True'

count = 50
while count > 0:
    print(f"countdown : {count}")
    count -= 1