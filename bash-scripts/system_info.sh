#!/bin/bash

echo "===== SYSTEM INFORMATION =====" > ../outputs/system_info.txt

echo "Date and Time:" >> ../outputs/system_info.txt
date >> ../outputs/system_info.txt

echo "" >> ../outputs/system_info.txt

echo "Disk Usage:" >> ../outputs/system_info.txt
df -h >> ../outputs/system_info.txt

echo "" >> ../outputs/system_info.txt

echo "Memory Usage:" >> ../outputs/system_info.txt
free -h >> ../outputs/system_info.txt

echo "" >> ../outputs/system_info.txt

echo "Running Processes:" >> ../outputs/system_info.txt
ps -aux >> ../outputs/system_info.txt

echo "System information collected successfully"
echo "Cron job executed at $(date)" >> /home/ubuntu/cloud-automation-project/outputs/cron_log.txt
