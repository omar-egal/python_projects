import boto3
import json
from datetime import datetime
from get_queue_url import *

#Get the current date & time
date_time = ("The time and date is: " + str(datetime.now()))

#send sqs message with the current date & time
def send_sqs_message():
    message = client.send_message(
        QueueUrl=url,
        MessageBody=date_time,
    )
