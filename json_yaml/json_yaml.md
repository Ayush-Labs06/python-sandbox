# Working with JSON and YAML in Python

This guide covers how to read, write, and work with JSON and YAML data in Python. These formats are used heavily in cloud configs, APIs, CI/CD pipelines, and compliance tooling.

---

## 1. What JSON and YAML Are

Both JSON and YAML are text formats used to store structured data.

- `JSON`: very common in APIs, cloud responses, and machine-to-machine data exchange
- `YAML`: common in configuration files such as Kubernetes manifests, GitHub Actions, and CI/CD pipelines

Example JSON:
```json
{
  "name": "Ayush",
  "role": "SA",
  "active": true
}
```

Example YAML:
```yaml
name: Ayush
role: SA
active: true
```

---

## 2. JSON in Python

Python has a built-in module called `json`, so you do not need to install anything extra for basic JSON work.

### Convert Python dict to JSON
```python
import json

user = {
    "name": "Ayush",
    "role": "SA",
    "active": True
}

json_data = json.dumps(user)
print(json_data)
```

### Convert JSON string to Python dict
```python
import json

json_data = '{"name": "Ayush", "role": "SA", "active": true}'
user = json.loads(json_data)

print(user["name"])
print(user["active"])
```

### Common JSON methods

| Method | Use |
| :--- | :--- |
| `json.dumps(data)` | Convert Python object to JSON string |
| `json.loads(text)` | Convert JSON string to Python object |
| `json.dump(data, file)` | Write JSON to a file |
| `json.load(file)` | Read JSON from a file |

---

## 3. Reading and Writing JSON Files

### Write JSON to a file
```python
import json

config = {
    "region": "us-east-1",
    "service": "s3",
    "encrypted": True
}

with open("config.json", "w") as f:
    json.dump(config, f, indent=4)
```

### Read JSON from a file
```python
import json

with open("config.json", "r") as f:
    config = json.load(f)

print(config["region"])
```

### Why `indent=4` is useful

It makes the JSON file easier for humans to read.

---

## 4. YAML in Python

YAML is not built into Python like `json`. You usually use the `PyYAML` package.

### Common import
```python
import yaml
```

### Convert Python dict to YAML
```python
import yaml

config = {
    "region": "us-east-1",
    "service": "s3",
    "encrypted": True
}

yaml_data = yaml.dump(config)
print(yaml_data)
```

### Convert YAML text to Python dict
```python
import yaml

yaml_data = """
region: us-east-1
service: s3
encrypted: true
"""

config = yaml.safe_load(yaml_data)
print(config["service"])
```

### Why `safe_load()` is preferred

Use `yaml.safe_load()` instead of `yaml.load()` for normal parsing. It avoids unsafe behavior and is the standard default for config files.

---

## 5. Reading and Writing YAML Files

### Write YAML to a file
```python
import yaml

pipeline = {
    "stage": "security-scan",
    "tool": "trivy",
    "enabled": True
}

with open("pipeline.yaml", "w") as f:
    yaml.dump(pipeline, f)
```

### Read YAML from a file
```python
import yaml

with open("pipeline.yaml", "r") as f:
    pipeline = yaml.safe_load(f)

print(pipeline["tool"])
```

---

## 6. JSON vs YAML

| Feature | JSON | YAML |
| :--- | :--- | :--- |
| Readability | More strict, more symbols | More human-friendly |
| Built into Python | Yes | No |
| Common Use | APIs, logs, cloud SDK output | Config files, IaC, pipelines |
| Comments | Not supported | Supported |

---

## 7. Cloud Security Use Cases

This topic matters directly for your learning path:

- AWS, Azure, and GCP APIs often return JSON
- IAM policies are usually JSON
- Kubernetes manifests are YAML
- GitHub Actions and many CI/CD files are YAML
- Security scan outputs are often JSON and then parsed by Python

Example:
```python
import json

finding = {
    "resource": "s3-bucket-prod",
    "public": True,
    "severity": "high"
}

if finding["public"]:
    print(f"Remediate {finding['resource']}")
```

---

## 8. Python vs JavaScript Cheat Sheet

| Feature | JavaScript | Python |
| :--- | :--- | :--- |
| Convert object to JSON string | `JSON.stringify(obj)` | `json.dumps(obj)` |
| Parse JSON string | `JSON.parse(text)` | `json.loads(text)` |
| Read JSON file | Common with `fs` + `JSON.parse()` | `json.load(file)` |
| YAML support | External package | External package like `PyYAML` |

---

## 9. Important Beginner Notes

- JSON `true`, `false`, `null` become Python `True`, `False`, `None`
- A JSON object usually becomes a Python `dict`
- A JSON array usually becomes a Python `list`
- YAML is indentation-sensitive, so spacing matters
- Use `json` first because it is built in and easier to start with
