import boto3

sns = boto3.client('sns')

try:
    response = sns.create_topic(
        Name='CloudAutomationAlerts'
    )

    topic_arn = response['TopicArn']

    sns.subscribe(
        TopicArn=topic_arn,
        Protocol='email',
        Endpoint='sussanekhan8@gmail.com'
    )

    print("SNS Topic and Email Subscription Created")

except Exception as e:
    print("Error:", e)
