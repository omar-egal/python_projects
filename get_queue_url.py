import boto3
from get_AWSaccount_id import *
client = boto3.client('sqs')

#Get SQS queue URL abd assign to a variable  
url = client.get_queue_url(
    QueueName='week15_standard_queue',
    QueueOwnerAWSAccountId=acc_id
)
url = url['QueueUrl']