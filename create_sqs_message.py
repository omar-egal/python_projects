import boto3
import json
from datetime import datetime
client = boto3.client('sqs')

#Get the current date & time
response = "The time and date is: "
date_time = datetime.now()

#send sqs message with the current date & time

message = client.send_message(
    QueueUrl='https://queue.amazonaws.com/191325089225/week15-sqs-queue',
    MessageBody=("This was processed on: " + str(date_time.strftime('%Y-%m-%d %H:%M:%S')))
    )
print((json.dumps(message, indent=2)))