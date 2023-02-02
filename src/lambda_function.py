import os
import boto3

dynamodb = boto3.client('dynamodb')

# Lambda function to handle the authentication request from AWS Transfer for SFTP
def lambda_handler(event, context):
    #Check if required parameters are present and connection is through SFTP
    if event['protocol'] != 'SFTP' and not event['username'] and not event['password']:
        return {}
    print("User " + event['username'] + "attempting to login...")
    #Get the user details from DynamoDB
    user = dynamodb.get_item(
        TableName=os.environ['USER_TABLE'],
        Key={'user': {'S': event ['username']}})
    #Check if user exists and password matches
    if 'Item' in user and user['Item']['password']['S'] == event['password']:
        print('Authentication successful')
        return {
            "Role": os.environ['IAM_ROLE'],
            "HomeDirectoryType": "LOGICAL",
            "HomeDirectoryDetails": '[{"Entry": "/", "Target": "/' + os.environ.get('BUCKET') + '/${transfer:UserName}"}]'
            }
    else:
        print('Authentication failed')
        return {}
    



