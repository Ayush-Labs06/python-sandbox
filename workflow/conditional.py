# Conditionals (if, elif, else)

age = int(input("Enter your age: "))

if age >=18:
    print("you are adult")
elif age > 12 and age < 18:
    print("You are teenager")
else:
    print("you are child")