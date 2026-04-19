# `try` and `except` : put risky code inside `try` if an error happens, python jumps to `except`

try:
    number = int("abc")
except ValueError:
    print("That is not a Valid Integer") # Program Continues
    
user = {"Ayush" : "Ayush"}

try:
    print(user["Age"])
except KeyError:
    print("Email Key is Missing")
    
    
# Else block runs only if no exception happened

try :
    number = int("25")
except ValueError:
    print("Conversion failed")
else:
    print(f"Conversion worked: {number}")
    
    
# `finally` block always run, regardless of error or not

try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("Finished file operation") # `with open(...)`
    
# we can catch error with `as`

try:
    result = 10 / 0
except ZeroDivisionError as error:
    print(f"Operation failed : {error}")
    
# ------------ --------------


finding = {
    "resource" : "s3-bucket-prod",
    "prublic" : True
}

try:
    if finding["public"]:
        print(f"Remediate {finding['resource']}")
except KeyError as error:
    print(f"Missing expected field: {error}")        