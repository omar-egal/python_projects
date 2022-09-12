import boto3
import json
from datetime import datetime

#Create a standard SQS queue for week 15 project
caller_id = boto3.client('sts')
client = boto3.client('sqs')
response = client.create_queue(
    QueueName='week15_standard_queue')

#Get AWS account ID  
acc_id = caller_id.get_caller_identity()
acc_id = acc_id['Account']


#Get SQS queue URL    
url = client.get_queue_url(
    QueueName='week15_standard_queue',
    QueueOwnerAWSAccountId=acc_id
)
url = url['QueueUrl']

#Get he current date & time
date_time = str(datetime.now())


#send sqs message with the current date & time
message = client.send_message(
    QueueUrl=url,
    MessageBody=date_time,
)
