# Introduction to Boto3

Boto3 is the AWS SDK for Python.
It lets you write Python code that talks to AWS services like S3, EC2, IAM, Lambda, and DynamoDB.
If the AWS Console is point-and-click, Boto3 is the programmable way to do the same work.

---

## 1. Why Boto3 Matters

You use Boto3 when you want to:

- automate repetitive AWS tasks
- build scripts for cloud operations
- collect AWS data for reporting or auditing
- integrate AWS actions into Python applications

Examples:

- list S3 buckets
- check EC2 instances
- read IAM users and roles
- upload files to S3

---

## 2. Install Boto3

Install it with pip:

```bash
pip install boto3
```

You usually also need AWS credentials configured on your machine.

```bash
aws configure
```

This stores your:

- access key
- secret key
- default region
- output format

---

## 3. First Import

```python
import boto3
```

That import gives you access to AWS service clients and resources.

---

## 4. Clients and Resources

Boto3 mainly works in two ways:

### Client

A client gives you low-level access to AWS service APIs.

```python
import boto3

s3 = boto3.client("s3")
response = s3.list_buckets()

print(response)
```

### Resource

A resource gives you a more object-oriented interface for some services.

```python
import boto3

s3 = boto3.resource("s3")

for bucket in s3.buckets.all():
    print(bucket.name)
```

In practice, many people start with `client` because it matches AWS API documentation more directly.

---

## 5. Your First Useful Call

One of the best first commands is `STS get_caller_identity`.
It tells you which AWS account and identity your code is using.

```python
import boto3

sts = boto3.client("sts")
identity = sts.get_caller_identity()

print(identity)
```

Typical output includes:

- `UserId`
- `Account`
- `Arn`

This is a very useful sanity check before calling other services.

---

## 6. Example: List S3 Buckets

```python
import boto3

s3 = boto3.client("s3")
response = s3.list_buckets()

for bucket in response["Buckets"]:
    print(bucket["Name"])
```

What is happening here:

- `boto3.client("s3")` creates an S3 client
- `list_buckets()` calls the AWS S3 API
- the response is a Python dictionary
- `response["Buckets"]` contains a list of bucket details

---

## 7. AWS Responses Are Usually Dictionaries

Most Boto3 calls return nested Python dictionaries and lists.

Example:

```python
import boto3
import json

sts = boto3.client("sts")
identity = sts.get_caller_identity()

print(json.dumps(identity, indent=2))
```

This is why Python dictionaries and JSON basics matter before learning Boto3 deeply.

---

## 8. Sessions

A session lets you control profile and region more explicitly.

```python
import boto3

session = boto3.Session(profile_name="default", region_name="us-east-1")
s3 = session.client("s3")
```

Use sessions when:

- working with multiple AWS accounts
- switching profiles
- writing cleaner multi-region scripts

---

## 9. Basic Error Handling

AWS calls can fail because of:

- wrong credentials
- missing permissions
- wrong region
- missing resource names

Basic example:

```python
import boto3
from botocore.exceptions import ClientError

s3 = boto3.client("s3")

try:
    response = s3.list_buckets()
    print(response["Buckets"])
except ClientError as e:
    print("AWS error:", e)
```

---

## 10. Good Habits from the Start

- Never hardcode AWS keys in source code
- Start with read-only API calls
- Use `get_caller_identity()` to verify your account
- Print and inspect responses before writing complex logic
- Add error handling for real scripts

---

## 11. Beginner Services to Practice

Good services to start with:

- `s3`
- `sts`
- `ec2`
- `iam`

These help you learn the main Boto3 patterns without too much complexity.

---

## 12. Simple Summary

Boto3 lets Python scripts communicate with AWS.
You usually create a client, call an API method, and process the returned dictionary.
Start with STS and S3, understand credentials and regions, then move into EC2 and IAM.
