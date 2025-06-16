import json
import boto3

s3 = boto3.client("s3")

def lambda_handler(event,context):
    bucket = "<bucket_name>"
    key = "key_name"
    response = s3.get_object(Bucket = bucket, key=key)
    content = response["Body"]

    jsonObject = json.loads(content.read())
    transactions = jsonObject["transactions"]

    for record in transactions:
        print(record["transactionId"])