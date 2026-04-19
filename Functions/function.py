def greet(name="User"):
    """This is a docstring that (optional) describe this function."""
    return f"Hello, {name}"

print(greet("Ayush")) #Hello, Ayush
print(greet()) # Hello, User (uses default)


# Lambda Functions : Short, one line functions
area_rectangle = lambda a,b : a * b
print(area_rectangle(4,5))

# Modules
# import math 
# print(math.sqrt(144))

# Selective Importing :
from math import pi,floor
print(floor(pi*3)) # 9

# Aliasing : 
import pandas as pd

data = {
    "name": ["Ayush", "Luke", "Witcher"],
    "score": [85, 90, 78]
}

df = pd.DataFrame(data)
print(df)
