import boto3

#Get AWS account ID and assign it to a variable
caller_id = boto3.client('sts')
acc_id = caller_id.get_caller_identity()
acc_id = acc_id['Account']