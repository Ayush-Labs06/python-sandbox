# Boto3 Learning Plan

This plan is meant to take you from Boto3 basics to writing useful AWS automation scripts with confidence.
Focus on learning one concept at a time, testing it in a small script, and understanding the AWS service you are calling.

---

## 1. Prerequisites

Before starting Boto3, be comfortable with:

- Python basics: variables, loops, functions, files, exceptions
- JSON: AWS APIs often return data as nested dictionaries and lists
- Basic AWS concepts: regions, IAM users/roles, services, and permissions
- CLI setup: `aws configure` and the meaning of access key, secret key, and default region

---

## 2. Phase 1: Understand What Boto3 Is

Goal: understand what Boto3 does and how it fits into AWS automation.

Topics to learn:

- What Boto3 is: the AWS SDK for Python
- Difference between SDK, API, CLI, and Console
- Why Boto3 is useful for automation and scripting
- Common use cases: listing S3 buckets, querying EC2 instances, reading Secrets Manager values, automating IAM checks

Practice:

- Install Boto3 with `pip install boto3`
- Configure AWS credentials with `aws configure`
- Run one simple script that creates an S3 client and lists buckets

---

## 3. Phase 2: Learn Clients and Resources

Goal: understand the two main ways to work with AWS services in Boto3.

Topics to learn:

- `boto3.client("service")`
- `boto3.resource("service")`
- When to use clients vs resources
- Why many newer examples prefer clients

Practice:

- Use an S3 client to call `list_buckets()`
- Use an S3 resource to iterate through buckets
- Compare the output and syntax

Expected outcome:

- You should know that clients map more directly to AWS APIs and resources offer a more object-style interface

---

## 4. Phase 3: Learn Authentication and Configuration

Goal: understand how Boto3 finds credentials and region settings.

Topics to learn:

- Default credential chain
- Environment variables
- `~/.aws/credentials` and `~/.aws/config`
- Named profiles with `boto3.Session(profile_name="dev")`
- Region selection and why it matters

Practice:

- Create a default session
- Create a named profile session
- Print the configured region from your session

Important note:

- Never hardcode access keys in source code

---

## 5. Phase 4: Read AWS Responses Properly

Goal: get comfortable reading nested AWS response data.

Topics to learn:

- AWS responses are usually Python dictionaries
- Common patterns: lists of dictionaries, metadata blocks, pagination
- Safe access with `.get()`
- Printing structured data with `json.dumps(..., indent=2, default=str)`

Practice:

- Call an EC2 or S3 API and inspect the raw response
- Extract only the fields you care about
- Convert the response into a smaller custom dictionary

---

## 6. Phase 5: Core Services to Learn First

Start with services that are common and easy to understand.

### S3

Learn:

- List buckets
- List objects
- Upload a file
- Download a file
- Delete an object

Why first:

- S3 is simple, common, and great for learning client calls

### EC2

Learn:

- Describe instances
- Filter by state or tag
- Read instance IDs, names, and public IPs

Why next:

- Good practice for nested response parsing

### IAM

Learn:

- List users
- List roles
- Read attached policies

Why it matters:

- IAM teaches permission-aware automation

### STS

Learn:

- Call `get_caller_identity()`

Why it matters:

- It is the easiest way to verify which account and identity your script is using

---

## 7. Phase 6: Error Handling and Safe Automation

Goal: write scripts that fail clearly and safely.

Topics to learn:

- `try` / `except`
- `botocore.exceptions.ClientError`
- Handling missing permissions
- Handling missing resources
- Logging useful messages

Practice:

- Write a script that catches `ClientError`
- Print the AWS error code and message
- Handle common issues like `AccessDenied` and `NoSuchBucket`

---

## 8. Phase 7: Pagination, Filters, and Efficiency

Goal: work with real AWS accounts that may contain large amounts of data.

Topics to learn:

- Paginators
- Filters
- Limiting fields you extract
- Avoiding unnecessary API calls

Practice:

- Use a paginator for `list_objects_v2` or another list API
- Filter EC2 instances by tag or state

---

## 9. Phase 8: Build Small Real Projects

Goal: turn isolated practice into practical automation.

Project ideas:

- List all S3 buckets and save the result to JSON
- Find stopped EC2 instances in a region
- Audit IAM users and attached policies
- Check your current AWS account with STS
- Download a file from S3 and process it locally

Expected outcome:

- You should be able to read requirements, choose the right service client, make API calls, and handle errors cleanly

---

## 10. Phase 9: Move Toward Intermediate Boto3

After basics, start learning:

- Sessions and multi-account access
- Cross-account role assumption with STS
- Waiters
- Upload/download options in S3
- Lambda invocation
- DynamoDB basic read/write operations
- CloudWatch logs retrieval

---

## 11. Suggested Learning Order

Use this order to stay practical:

1. Boto3 overview
2. Install and configure AWS credentials
3. Sessions, clients, and resources
4. S3 basics
5. STS identity check
6. EC2 describe calls
7. IAM read-only scripts
8. Error handling
9. Pagination and filtering
10. Small automation projects

---

## 12. Recommended Practice Routine

For each topic:

1. Read the concept
2. Write one short script
3. Run it against a safe AWS account or sandbox
4. Inspect the returned data
5. Rewrite the script more cleanly

Keep each script small and focused.

---

## 13. Common Mistakes to Avoid

- Hardcoding credentials in code
- Using admin credentials for practice
- Ignoring region settings
- Not reading the raw API response carefully
- Writing scripts without exception handling
- Testing destructive actions before understanding the API

---

## 14. End Goal

By the end of this plan, you should be able to:

- Authenticate to AWS safely
- Use Boto3 clients to call service APIs
- Read and filter AWS response data
- Handle common errors
- Build simple automation scripts for S3, EC2, IAM, and STS
