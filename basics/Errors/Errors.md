# Error Handling in Python

Error handling lets your program deal with problems without crashing immediately. In Python, this is usually done with `try`, `except`, `else`, and `finally`.

---

## 1. Why Error Handling Matters

Programs fail for many normal reasons:

- a file does not exist
- JSON is malformed
- user input is invalid
- an API call fails
- a key is missing in a dictionary

In cloud security automation, this matters a lot. A script may read config files, call AWS APIs, parse responses, and remediate issues. If one step fails, you want a clear message and controlled behavior.

---

## 2. Basic `try` and `except`

Put risky code inside `try`. If an error happens, Python jumps to `except`.

```python
try:
    number = int("abc")
except ValueError:
    print("That is not a valid integer.")
```

Explanation:

- `int("abc")` raises a `ValueError`
- the `except` block catches it
- the program continues instead of stopping with a traceback

---

## 3. Common Exception Types

| Exception | When it Happens | Example |
| :--- | :--- | :--- |
| `ValueError` | Right type, wrong value | `int("abc")` |
| `TypeError` | Wrong type used | `"2" + 2` |
| `KeyError` | Missing dictionary key | `user["email"]` |
| `IndexError` | List index out of range | `items[10]` |
| `FileNotFoundError` | File does not exist | `open("missing.txt")` |
| `ZeroDivisionError` | Division by zero | `10 / 0` |

Example:

```python
user = {"name": "Ayush"}

try:
    print(user["email"])
except KeyError:
    print("Email key is missing.")
```

---

## 4. Catching Multiple Exceptions

You can handle different errors in different ways.

```python
try:
    value = int(input("Enter a number: "))
    result = 10 / value
    print(result)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
```

This is better than using one broad `except` when the recovery message should depend on the error.

---

## 5. Using `else`

The `else` block runs only if no exception happened.

```python
try:
    number = int("25")
except ValueError:
    print("Conversion failed.")
else:
    print(f"Conversion worked: {number}")
```

Use `else` for code that should run only after success.

---

## 6. Using `finally`

The `finally` block always runs, whether an error happened or not.

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Finished file operation.")
```

This is useful for cleanup, such as:

- closing files
- releasing connections
- logging completion

Note: in modern Python, `with open(...)` is usually better for files because it handles closing automatically.

---

## 7. Catching the Error Object

You can inspect the actual error message using `as`.

```python
try:
    result = 10 / 0
except ZeroDivisionError as error:
    print(f"Operation failed: {error}")
```

This helps with debugging and logging.

---

## 8. A Real Example with Files and JSON

This is closer to real automation work.

```python
import json

try:
    with open("config.json", "r") as file:
        config = json.load(file)
except FileNotFoundError:
    print("Config file is missing.")
except json.JSONDecodeError:
    print("Config file contains invalid JSON.")
else:
    print("Config loaded successfully.")
    print(config)
```

Why this matters:

- missing file: maybe the deployment forgot to include it
- invalid JSON: maybe someone edited it incorrectly

---

## 9. Cloud Security Example

Imagine you are checking a security finding from a config file.

```python
finding = {
    "resource": "s3-bucket-prod",
    "public": True
}

try:
    if finding["public"]:
        print(f"Remediate {finding['resource']}")
except KeyError as error:
    print(f"Missing expected field: {error}")
```

In real cloud scripts, missing fields are common when:

- API responses change
- optional fields are absent
- input data is incomplete

---

## 10. Avoid Bare `except`

This is risky:

```python
try:
    do_something()
except:
    print("Something went wrong.")
```

Why it is bad:

- it catches almost everything
- it hides the real issue
- debugging becomes harder

Prefer specific exceptions:

```python
try:
    do_something()
except ValueError:
    print("Invalid value.")
```

---

## 11. Raising Your Own Errors

You can intentionally raise an error when input is invalid.

```python
age = -1

if age < 0:
    raise ValueError("Age cannot be negative.")
```

This is useful when your code detects bad data and should stop early.

---

## 12. Python vs JavaScript Cheat Sheet

| Feature | JavaScript | Python |
| :--- | :--- | :--- |
| Basic syntax | `try {}` / `catch (e) {}` | `try:` / `except:` |
| Success block | no direct `else` | `else:` |
| Always-run block | `finally` | `finally` |
| Throw error | `throw new Error("msg")` | `raise ValueError("msg")` |

---

## 13. Important Beginner Notes

- Errors are normal; handling them is part of writing reliable code
- Use specific exception types whenever possible
- Use `else` for success-only code
- Use `finally` for cleanup
- Prefer clear error messages over silent failure
- In automation, handle file, parsing, and API-related errors carefully
