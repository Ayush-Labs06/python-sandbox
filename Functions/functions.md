# Functions and Modules in Python

Functions allow you to bundle code into reusable blocks. Modules allow you to organize those functions across different files.

---

## 1. Defining Functions (`def`)

In Python, we use the `def` keyword to define a function.

```python
def greet(name="User"):
    """This is a docstring (optional) that describes the function."""
    return f"Hello, {name}!"

# Calling the function
print(greet("Ayush"))  # Hello, Ayush!
print(greet())         # Hello, User! (uses default)
```

### Key Features:
*   **Indentation:** Like loops, the function body must be indented.
*   **Return:** Functions return `None` by default if no `return` statement is used.
*   **Default Arguments:** You can set default values for parameters.
*   **Keyword Arguments:** You can call functions using parameter names: `greet(name="Ayush")`.

---

## 2. Lambda Functions (Anonymous)

Short, one-line functions that don't need a name.

```python
# Standard:
def square(x): return x * x

# Lambda:
square_lambda = lambda x: x * x

print(square_lambda(5)) # 25
```

---

## 3. Modules (`import`)

A module is just a `.py` file containing Python code. You can use code from one file in another.

### Basic Import
```python
import math
print(math.sqrt(16)) # 4.0
```

### Selective Import
```python
from math import pi, floor
print(floor(pi)) # 3
```

### Aliasing
```python
import pandas as pd
import datetime as dt
```

---

## 4. The `if __name__ == "__main__":` Pattern

This ensures that certain code *only* runs if the file is executed directly, not when it's imported as a module.

```python
def main_logic():
    print("Running main logic!")

if __name__ == "__main__":
    main_logic()
```

---

## Python vs. JS Cheat Sheet

| Feature | JavaScript | Python |
| :--- | :--- | :--- |
| **Definition** | `function name() {}` or `const name = () => {}` | `def name():` |
| **Arrow Function** | `(x) => x * x` | `lambda x: x * x` |
| **Import** | `import { x } from 'mod'` | `from mod import x` |
| **Export** | `export const x = ...` | Everything in a `.py` file is exported by default |
| **Default Args** | `function(n = "User")` | `def greet(n="User"):` |
