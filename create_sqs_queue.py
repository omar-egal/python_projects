import boto3

#Create a standard SQS queue for week 15 project
client = boto3.client('sqs')
response = client.create_queue(
    QueueName='week15_standard_queue')
