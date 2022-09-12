import boto3
import json
from get_queue_url import *

sqs = boto3.client('sqs')
response = sqs.receive_message(
    QueueUrl=url,
)

messages = response['Messages']
for message in messages:
    print(json.dumps(message['Body'], indent=2, default=str))