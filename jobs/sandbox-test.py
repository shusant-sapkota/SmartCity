import boto3

# Initialize a boto3 STS client
sts_client = boto3.client('sts')

# Assume a role to get temporary credentials
# response = sts_client.assume_role(
#     RoleArn='arn:aws:iam::123456789012:role/YourRoleName',
#     RoleSessionName='pyspark-session'
# )

# Extract temporary credentials
# credentials = response['Credentials']
# access_key = credentials['AccessKeyId']
# secret_key = credentials['SecretAccessKey']
# session_token = credentials['SessionToken']

# Using that provided from the sandbox
access_key = ''
secret_key = ''
session_token = ''

s3_client = boto3.client(
    's3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    aws_session_token=session_token
)

# Specify the bucket name
bucket_name = 'ss-spark-streaming-data'

# List all files in the specified S3 bucket
response = s3_client.list_objects_v2(Bucket=bucket_name)

# Check if 'Contents' key exists in the response
if 'Contents' in response:
    for obj in response['Contents']:
        print(obj['Key'])
else:
    print('No files found in the bucket.')