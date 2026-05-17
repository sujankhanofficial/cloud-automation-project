import boto3
import logging

logging.basicConfig(
    filename='logs/s3.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

s3 = boto3.client('s3')

bucket_name = 'sujan-cloud-backup-2026'

try:
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'us-east-2'
        }
    )

    print("S3 Bucket Created Successfully")
    logging.info("S3 bucket created successfully")

except Exception as e:
    print("Error:", e)
    logging.error(str(e))
