import boto3
import logging

logging.basicConfig(
    filename='../logs/ec2.log',
    level=logging.INFO
)

try:
    ec2 = boto3.resource('ec2')

    instances = ec2.create_instances(
        ImageId='ami-0eab37cfdc33e8e65',
        MinCount=1,
        MaxCount=1,
        InstanceType='t3.micro'
    )

    print("EC2 Instance Created Successfully")

    logging.info("EC2 created successfully")

except Exception as e:
    print("Error:", e)
    logging.error(str(e))
