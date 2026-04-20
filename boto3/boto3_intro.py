import boto3,json

# Clien based low-level access to AWS services
s3 = boto3.client("s3")
s3_bucket_list = s3.list_buckets()
print(json.dumps(s3_bucket_list, indent=4, default=str))

# Resource based giving more objected oriented interface for some sevices

s3_res = boto3.resource("s3")

for bucket in s3_res.buckets.all():
    print(bucket.name)
    

# STS get called identity : Enlist the authenticatd aws account

sts = boto3.client("sts")
identity = sts.get_caller_identity()

print(identity)

# Sessions : Allows to control profile and region

session = boto3.Session(region_name="ap-south-1")
s3 = session.client("s3") # ..... Multi regions scripts


# Error Handling

'''
AWS calls can fail because of :

- wrong credentials
- missing permissions
- wrong region
- missing resource names

'''

from botocore.exceptions import ClientError

s3 = boto3.client("s3")

try:
    response = s3.list_buckets()
    print(response["Buckets"])
except ClientError as e:
    print("AWS error:", e)