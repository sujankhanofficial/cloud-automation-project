# Cloud Automation Scripting Project

## Introduction

This project is based on cloud automation using AWS services, Python scripting, Bash scripting, AWS CLI, cron jobs, and Git version control.

The main goal of this project is to automate cloud provisioning and monitoring tasks instead of doing everything manually.

---

# AWS Services Used

- EC2
- S3
- IAM
- CloudWatch
- SNS

---

# Tools and Technologies Used

- Python
- Bash Scripting
- boto3
- AWS CLI
- Cron Jobs
- Git
- Ubuntu EC2 Instance

---

# Project Tasks Completed

## 1. EC2 Automation

Created a Python script to automatically launch an EC2 instance using boto3.

File:
python-scripts/create_ec2.py

---

## 2. S3 Bucket Automation

Created a Python script to automatically create an S3 bucket.

File:
python-scripts/create_s3.py

---

## 3. File Backup to S3

Uploaded sample files into S3 bucket using Python automation.

File:
python-scripts/backup_s3.py

---

## 4. IAM User Automation

Created IAM user automatically using Python script.

File:
python-scripts/create_iam_user.py

---

## 5. CloudWatch Monitoring

Created CPU utilization alarm using CloudWatch.

File:
python-scripts/create_alarm.py

---

## 6. SNS Notification

Created SNS topic for cloud notifications.

File:
python-scripts/create_sns.py

---

## 7. Bash Automation Script

Created Bash script to collect:
- system information
- disk usage
- memory usage
- running processes

File:
bash-scripts/system_info.sh

---

## 8. Scheduled Automation using Cron

Configured cron job to run Bash script automatically every 5 minutes.

Cron Job:

*/5 * * * * /home/ubuntu/cloud-automation-project/bash-scripts/system_info.sh

---

## 9. Logging

Generated logs for cron execution and system information.

Output files:
- outputs/system_info.txt
- outputs/cron_log.txt

---

## 10. Git Version Control

Initialized Git repository and committed all project files.

Commands used:
- git init
- git add .
- git commit

---

# Project Folder Structure

cloud-automation-project/

├── bash-scripts/

│ └── system_info.sh

├── python-scripts/

│ ├── create_ec2.py

│ ├── create_s3.py

│ ├── backup_s3.py

│ ├── create_iam_user.py

│ ├── create_alarm.py

│ └── create_sns.py

├── outputs/

│ ├── system_info.txt

│ └── cron_log.txt

├── logs/

│ └── ec2.log

└── README.md

---

# Example Outputs

- EC2 instance created successfully
- S3 bucket created successfully
- IAM user created successfully
- CloudWatch alarm created successfully
- Cron logs generated automatically
- System information collected successfully

---

# Conclusion

This project helped me understand cloud automation using AWS services, Python scripting, Bash scripting, monitoring, scheduling, logging, and Git version control.
