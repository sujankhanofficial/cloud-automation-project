import boto3

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

except Exception as e:
    print("Error:", e)
