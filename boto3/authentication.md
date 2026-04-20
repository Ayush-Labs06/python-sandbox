# Phase 3: Authentication and Configuration

## How Boto3 Finds Your Credentials

Boto3 does not require you to pass credentials explicitly. It searches for them in a fixed order called the **credential chain**. It stops at the first match it finds.

Order:
1. Explicitly passed in code (`aws_access_key_id=`, `aws_secret_access_key=`)
2. Environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`)
3. AWS credentials file (`~/.aws/credentials`)
4. AWS config file (`~/.aws/config`)
5. IAM role attached to EC2/Lambda/ECS (only works on AWS infrastructure)

In practice, you will almost always use option 2 or 3.

---

## The Credentials File

Running `aws configure` writes to `~/.aws/credentials`:

```
[default]
aws_access_key_id = AKIA...
aws_secret_access_key = ...

[dev]
aws_access_key_id = AKIA...
aws_secret_access_key = ...

[prod]
aws_access_key_id = AKIA...
aws_secret_access_key = ...
```

Each block in brackets is a **named profile**. `default` is used when you do not specify one.

---

## Environment Variables

Set these in your shell before running a script:

```bash
export AWS_ACCESS_KEY_ID=AKIA...
export AWS_SECRET_ACCESS_KEY=...
export AWS_DEFAULT_REGION=ap-south-1
```

Boto3 picks them up automatically. Useful in CI/CD pipelines and Docker containers.

---

## Using Named Profiles with Sessions

You already used `boto3.session` in your intro script. Here is how profiles fit in:

```python
import boto3

# Uses the [default] profile
session = boto3.Session()

# Uses the [dev] profile from ~/.aws/credentials
dev_session = boto3.Session(profile_name="dev")

# Check which region and credentials the session resolved to
print(dev_session.region_name)
print(dev_session.get_credentials().get_frozen_credentials())
```

A `Session` object holds configuration (profile, region, credentials) and can create multiple clients from it:

```python
s3 = dev_session.client("s3")
ec2 = dev_session.client("ec2")
sts = dev_session.client("sts")
```

---

## Region Selection

Region must be set or Boto3 will raise a `NoRegionError` for most services.

Ways to set it (same precedence order as credentials):

1. Passed directly: `boto3.client("s3", region_name="us-east-1")`
2. Session: `boto3.Session(region_name="ap-south-1")`
3. Environment variable: `AWS_DEFAULT_REGION`
4. Config file: `~/.aws/config` under `[default]` → `region = ap-south-1`

---

## Inspecting Your Resolved Configuration

```python
import boto3

session = boto3.Session()

# Print resolved region
print("Region:", session.region_name)

# Print the profile being used
print("Profile:", session.profile_name)

# Print resolved credentials (never log these in real scripts)
creds = session.get_credentials().get_frozen_credentials()
print("Key ID:", creds.access_key[:8], "...")
```

---

## Never Do This

```python
# BAD — hardcoded credentials in source code
s3 = boto3.client(
    "s3",
    aws_access_key_id="AKIAIOSFODNN7EXAMPLE",
    aws_secret_access_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
)
```

If this ends up in git, your keys are compromised. Always use the credential chain.

---

## Practice Tasks

1. Run `aws configure --profile sandbox` and set up a second profile.
2. Create a `boto3.Session(profile_name="sandbox")` and print its region.
3. Create an S3 client from that session and call `list_buckets()`.
4. Set `AWS_DEFAULT_REGION` as an environment variable and verify `session.region_name` picks it up.
5. Call `sts.get_caller_identity()` from two different sessions (two profiles) and compare the `Account` field.

---

## What Is Next

Next: **Phase 4 — Reading AWS Responses**

You will learn to navigate nested response dictionaries, extract only what you need, and print structured data cleanly.
