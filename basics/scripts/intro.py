print("This print word as it is")
print(3+2)

#Variables : Variables are used to store information to be referenced and manupulated in a program

# 1) init : Integeres (whole numbers)
intA = 8
intB = 9
sum = intA + intB
print(sum)

# 2) float : Floating point numbers (decimals)

mass = 71.2 
Acc = 9.8

print(f"weight : {mass * Acc}")

# 3) str : string(text)

service = "s3"
description = "simple storage service is AWS block storage service"
cost = "affordable"

print(f"Plan is to use {service} which is {description}")

# 4) bool : True or False booleans

if cost == "affordable" :
    buy = True
    
if buy:
    print("Service can be purchased")


