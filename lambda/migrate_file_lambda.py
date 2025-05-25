# Lambda function to copy S3 files and notify Glue
import boto3
import json
 
# Get the S3 client
s3 = boto3.client('s3')
 
def lambda_handler(event, context):
    # Get the list of records from the event
    print(event)
    records = event['Records']
 
    # Iterate through the records and copy the files from the source bucket to the destination bucket
    for record in records:
        di = record['body']
        result = json.loads(di)
        message=json.loads(result['Message'])
        source_bucket = message['Records'][0]['s3']['bucket']['name']
        key = message['Records'][0]['s3']['object']['key']
        print('key',key)
        copy_source = {'Bucket': source_bucket, 'Key': key}
        s3.copy_object(Bucket='Your-Target-S3-Bucket-Name', CopySource=copy_source, Key=key)
        print('File moved successfully')