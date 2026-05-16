import boto3

s3 = boto3.client('s3')

file_name = 'sample.txt'
bucket_name = 'sujan-cloud-backup-2026'

try:
    s3.upload_file(file_name, bucket_name, file_name)

    print("Backup Uploaded Successfully")

except Exception as e:
    print("Error:", e)
