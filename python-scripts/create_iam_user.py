import boto3
import logging

logging.basicConfig(
    filename='logs/iam.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

iam = boto3.client('iam')

try:
    response = iam.create_user(
        UserName='automation-user'
    )

    print("IAM User Created Successfully")
    logging.info("IAM user created successfully")

except Exception as e:
    print("Error:", e)
    logging.error(str(e))
