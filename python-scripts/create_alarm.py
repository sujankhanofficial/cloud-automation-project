import boto3

cloudwatch = boto3.client('cloudwatch')

try:
    cloudwatch.put_metric_alarm(
        AlarmName='HighCPUUsage',
        ComparisonOperator='GreaterThanThreshold',
        EvaluationPeriods=1,
        MetricName='CPUUtilization',
        Namespace='AWS/EC2',
        Period=300,
        Statistic='Average',
        Threshold=70.0,
        ActionsEnabled=False,
        AlarmDescription='Alarm when CPU exceeds 1%',
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': 'i-02786a6c300709efc'
            },
        ],
        Unit='Percent'
    )

    print("CloudWatch Alarm Created Successfully")

except Exception as e:
    print("Error:", e)
