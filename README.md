# Password-Enabled SFTP Server for S3 Buckets in AWS

#### This solution deploys an AWS Transfer server that authenticates users using a Lambda Function. The Lambda function checks the DynamoDB table for the user's password. If the password is correct, the user is granted access to the S3 bucket. If the password is incorrect, the user is denied access. The DynamoDB table is a key-value store where the key is the username and the value is the password. The Lambda function is written in Python and uses the Boto3 library to interact with AWS services.

#### AWS Resources Deployed: 
- Lambda Function
- DynamoDB table
- AWS Transfer Server
- IAM Permissions 

#### How to use:
1. Download and install AWS SAM CLI. 
2. Inside the project directory, run `sam build` to build the project.
3. Run `sam deploy --guided` to deploy the project.
4. Follow the prompts to deploy the project.
