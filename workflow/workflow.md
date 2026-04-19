# Control Flow in Python

This guide covers how to control the "logic flow" of your program using conditionals and loops.

---

## 1. Conditionals (`if`, `elif`, `else`)

In Python, we use indentation (tabs or spaces) instead of curly braces `{}` to define blocks of code.

### Basic Syntax
```python
age = 19

if age >= 18:
    print("You are an adult.")
elif age > 12:
    print("You are a teenager.")
else:
    print("You are a child.")
```

### Key Differences from JS:
*   **No Parentheses:** You don't need `()` around the condition.
*   **Colons:** Every branch must end with a colon `:`.
*   **`elif`:** Instead of `else if`, Python uses the shorthand `elif`.
*   **Logical Operators:** Instead of `&&` and `||`, Python uses literal words: `and`, `or`, `not`.

---

## 2. For Loops

`for` loops in Python are primarily used to iterate over a collection (like a List or Dictionary) or a range of numbers.

### Iterating over a List
```python
tools = ["S3", "EC2", "Lambda"]

for tool in tools:
    print(f"Deploying {tool}...")
```

### Using `range()`
If you need to loop a specific number of times (like `for(i=0; i<5; i++)` in JS):

*   `range(stop)`: Loops from 0 up to (but not including) `stop`.
*   `range(start, stop)`: Loops from `start` up to `stop`.
*   `range(start, stop, step)`: Loops from `start` up to `stop`, incrementing by `step`.

```python
# range(stop) - Prints 0, 1, 2, 3, 4
for i in range(5):
    print(i) 

# range(start, stop) - Prints 2, 3, 4, 5
for i in range(2, 6):
    print(i)

# range(start, stop, step) - Prints 0, 2, 4, 6, 8, 10
for i in range(0, 11, 2):
    print(i)
```

### Using `enumerate()`
Use `enumerate()` when you need both the **index** and the **value** of an item at the same time. This is cleaner than using `range(len(...))`.

```python
roles = ["SA", "manager", "Witcher"]

for i, role in enumerate(roles, start=1):
    print(f"{i} : {role}")

# Output:
# 1 : SA
# 2 : manager
# 3 : Witcher
```

### Iterating over a Dictionary
To loop through both keys and values in a dictionary, use `.items()`.

```python
user = {"name": "Ayush", "role": "SA", "id": 1}

for key, value in user.items():
    print(f"{key} -> {value}")
```

### Using `zip()`
Use `zip()` to iterate over two or more lists in parallel.

```python
names = ["Ayush", "Luke"]
roles = ["SA", "Manager"]

for name, role in zip(names, roles):
    print(f"{name} is a {role}")
```

### List Comprehensions
A concise way to create lists. It's often used instead of a loop to transform or filter data.

```python
# Create a list of squares for even numbers
numbers = range(10)
squares = [x**2 for x in numbers if x % 2 == 0]
# Result: [0, 4, 16, 36, 64]
```

---

## 3. While Loops

`while` loops run as long as a condition remains `True`.

```python
count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1 # Python doesn't have count--
```

---

## 4. Break and Continue

*   **`break`:** Exits the loop immediately.
*   **`continue`:** Skips the rest of the current loop and moves to the next iteration.

```python
for n in range(10):
    if n == 3:
        continue # Skip 3
    if n == 7:
        break    # Stop at 7
    print(n)
```

---

## Python vs. JS Cheat Sheet

| Feature | JavaScript | Python |
| :--- | :--- | :--- |
| **Logic And** | `&&` | `and` |
| **Logic Or** | `||` | `or` |
| **Logic Not** | `!` | `not` |
| **Else If** | `else if` | `elif` |
| **Strict Equality** | `===` | `==` (Python's `==` checks value equality) |
| **Increment** | `i++` | `i += 1` |
