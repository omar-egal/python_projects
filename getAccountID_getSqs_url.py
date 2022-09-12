import boto3
client = boto3.client('sqs')
caller_id = boto3.client('sts')

#Get AWS account ID and assign it to a variable
def get_account_id():
    acc_id = caller_id.get_caller_identity()
    acc_id = acc_id['Account']
    return acc_id
#Get SQS queue URL abd assign to a variable
def get_sqs_url():
    url = client.get_queue_url(
        QueueName='week15_standard_queue',
        QueueOwnerAWSAccountId=get_account_id()
    )
    url = url['QueueUrl']
    return url
