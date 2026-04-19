import yaml

config = {
    "region": "us-east-1",
    "service": "s3",
    "encrypted": True
}

# Converting python dist to YAML
yaml_data = yaml.dump(config)
print(yaml_data)

# convert YAML text to python dict
yaml_data = """
region: us-east-1
service: s3
encrypted: true
"""
config = yaml.safe_load(yaml_data)
print(config)