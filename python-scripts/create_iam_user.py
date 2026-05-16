import boto3

iam = boto3.client('iam')

try:
    response = iam.create_user(
        UserName='automation-user'
    )

    print("IAM User Created Successfully")

except Exception as e:
    print("Error:", e)
