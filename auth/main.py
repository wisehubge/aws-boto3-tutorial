"""
export AWS_ACCESS_KEY_ID="access-key"
export AWS_SECRET_ACCESS_KEY="secret-access-key"
export AWS_REGION="us-east-1"
"""
import os
import boto3

session = boto3.Session(
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

ec2 = session.resource("ec2")
for instance in ec2.instances.all():
    print("Instance ID:", instance.id)
    print("Arch", instance.architecture)
    print("Image", instance.image)
