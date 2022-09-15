import boto3
import json
from create_sqs_queue import *

sqs = boto3.client('sqs')
response = sqs.receive_message(
    QueueUrl=get_account_id(),
)

messages = response['Messages']
for message in messages:
    print(json.dumps(message['Body'], indent=2, default=str))