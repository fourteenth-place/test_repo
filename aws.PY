import boto3

s3 = boto3.resource("s3")

# client = boto3.client()
# client.

# To get list of buckets present in AWS using S3 client
def get_buckets_client():
   session = boto3.session.Session()
   # User can pass customized access key, secret_key and token as well
   s3_client = session.client('s3', aws_access_key_id="AKIA5N7WETETPK5H5TVB", 
                              aws_secret_access_key="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")
   response = s3_client.list_buckets()
   buckets =[]
   for bucket in response['Buckets']:
       buckets += {bucket["Name"]}

print(get_buckets_client())