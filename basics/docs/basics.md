# Python Basics

This guide covers the fundamental building blocks of Python.

## 1. Variables and Data Types

Variables are used to store information to be referenced and manipulated in a program.

### Common Data Types
| Type | Description | Example |
| :--- | :--- | :--- |
| `int` | Integers (whole numbers) | `x = 10` |
| `float` | Floating-point numbers (decimals) | `y = 3.14` |
| `str` | Strings (text) | `name = "Python"` |
| `bool` | Boolean (True or False) | `is_active = True` |
| `list` | Ordered collection of items | `fruits = ["apple", "banana"]` |
| `dict` | Key-value pairs | `person = {"name": "Ayush", "age": 25}` |

---

## 2. Basic Operations

Python supports various operators for performing calculations and logic.

### Arithmetic Operators
- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division (results in a float)
- `//` Floor Division (results in an integer)
- `%` Modulus (remainder)
- `**` Exponentiation (power)

### Comparison Operators
- `==` Equal to
- `!=` Not equal to
- `>` Greater than
- `<` Less than
- `>=` Greater than or equal to
- `<=` Less than or equal to

---

## 3. Strings and String Operations

Strings are sequences of characters enclosed in single, double, or triple quotes.

### Common String Methods
- `.upper()`: Converts to uppercase.
- `.lower()`: Converts to lowercase.
- `.strip()`: Removes leading/trailing whitespace.
- `.split(separator)`: Splits string into a list.
- `.join(iterable)`: Joins elements of an iterable into a string.
- `.replace(old, new)`: Replaces a substring.

### String Slicing and Indexing
```python
s = "Python Basics"
print(s[0])      # 'P' (Indexing)
print(s[0:6])    # 'Python' (Slicing: [start:end])
print(s[-1])     # 's' (Negative Indexing)
```

### String Formatting
```python
name = "Ayush"
age = 25

# f-strings (Modern and preferred)
print(f"My name is {name} and I am {age} years old.")

# .format() method
print("Name: {}, Age: {}".format(name, age))
```
