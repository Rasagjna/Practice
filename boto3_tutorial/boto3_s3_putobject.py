import json
import boto3

s3 = boto3.client("s3")

def lambda_handler(event,context):
    bucket = "<bucket_name>"
    key = "key_name"
    transactionTOUpload = {}
    transactionTOUpload["trenactinId"] = "purchase"
    fileName = "<file_name.json>"

    uploadByteStream = bytes(json.dumps(transactionTOUpload).encode("UTF-8"))
    s3.put_object(Bucket = bucket, Key=key,Body = uploadByteStream)

    print("complete")