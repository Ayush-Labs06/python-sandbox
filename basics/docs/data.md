# Data Structures in Python: Lists and Dictionaries

This document provides a deep dive into the two most commonly used collection types in Python.

---

## 1. Lists (`list`)

A **List** is an ordered, mutable (changeable) collection of items. It allows duplicate members.

### When to use a List?
*   When the **order** of items matters.
*   When you need a simple **sequence** of items (e.g., a list of filenames, a queue of tasks).
*   When you need to frequently add or remove items from the end of the collection.

### Key Syntax and Operations

| Operation | Syntax | Description |
| :--- | :--- | :--- |
| **Creation** | `my_list = [1, 2, 3]` | Square brackets define a list. |
| **Access** | `my_list[0]` | Access by index (starts at 0). |
| **Slicing** | `my_list[1:3]` | Get a sub-section (from index 1 up to, but not including, 3). |
| **Append** | `my_list.append(4)` | Adds an item to the very end. |
| **Insert** | `my_list.insert(0, "hi")` | Adds "hi" at index 0, shifting others. |
| **Remove** | `my_list.remove(2)` | Removes the *first* occurrence of the value `2`. |
| **Pop** | `val = my_list.pop()` | Removes and returns the last item. |
| **Length** | `len(my_list)` | Returns the number of items. |

---

## 2. Dictionaries (`dict`)

A **Dictionary** is a collection of Key-Value pairs. It is mutable and indexed by keys (which must be unique).

### When to use a Dictionary?
*   When you want to **map** one piece of data to another (e.g., User ID -> User Name).
*   When you need **fast lookups**. Finding a value by its key is extremely efficient in Python.
*   When your data has a **labeled structure** (e.g., a database record or a config file).

### Key Syntax and Operations

| Operation | Syntax | Description |
| :--- | :--- | :--- |
| **Creation** | `my_dict = {"id": 1, "name": "Ayush"}` | Curly braces with `key: value` pairs. |
| **Access** | `my_dict["id"]` | Access value by its key. Crashes if key doesn't exist. |
| **Safe Access** | `my_dict.get("age", 25)` | Returns value if key exists, otherwise returns default (25). |
| **Add/Update** | `my_dict["role"] = "Dev"` | If "role" exists, it updates; if not, it adds it. |
| **Delete** | `del my_dict["name"]` | Removes the key and its associated value. |
| **Keys** | `my_dict.keys()` | Returns a view of all keys. |
| **Values** | `my_dict.values()` | Returns a view of all values. |
| **Items** | `my_dict.items()` | Returns a view of `(key, value)` tuples. |

---

## List vs. Dictionary: Summary

| Feature | List (`[]`) | Dictionary (`{}`) |
| :--- | :--- | :--- |
| **Access method** | By Index (integer) | By Key (string, int, etc.) |
| **Ordering** | Maintains insertion order | Maintains insertion order (since Python 3.7+) |
| **Performance** | Fast access by index | Fast access by key |
| **Duplicates** | Allows duplicate values | Values can be duplicates; Keys MUST be unique |

---

## 3. Python vs. JavaScript (The "Aha!" Section)

If you're coming from JavaScript, here's how to translate your knowledge:

### Lists = Arrays
*   **JS:** `myArray.push(x)` $\rightarrow$ **Python:** `my_list.append(x)`
*   **JS:** `myArray.length` $\rightarrow$ **Python:** `len(my_list)`
*   **JS:** `myArray[0]` $\rightarrow$ **Python:** `my_list[0]`

### Dictionaries = Objects
*   **JS:** `{ name: "Ayush" }` $\rightarrow$ **Python:** `{ "name": "Ayush" }` (Note: Keys **must** be quoted in Python)
*   **JS:** `obj.name` $\rightarrow$ **Python:** `obj["name"]` (**No dot notation for dicts!**)

---

## 4. Nested Structures (Dict of Lists)

You can nest these structures just like in JS objects.

```python
# A dictionary where each key maps to a list
user_data = {
    "ayush": ["S3", "EC2", "Lambda"],
    "admin": ["IAM", "CloudTrail"]
}

# Accessing a nested item
first_service = user_data["ayush"][0] # Returns "S3"
```

---

## 5. Pro "Finesses" (The Cool Stuff)

### Negative Indexing
Python lets you count from the end of a list using negative numbers.
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[-1]) # "cherry" (last item)
print(fruits[-2]) # "banana" (second to last)
```

### The `.get()` Method (Dicts)
In JS, `obj.nonExistent` returns `undefined`. In Python, `dict["nonExistent"]` **crashes** your program. Use `.get()` to be safe:
```python
# Returns "Guest" if "user" key doesn't exist
username = user_dict.get("user", "Guest") 
```

### Membership Testing
Check if an item exists in a collection instantly using `in`.
```python
if "apple" in fruits:
    print("Found it!")

if "name" in user_dict:
    print("Key exists!")
```
