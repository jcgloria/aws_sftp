# Password-Enabled SFTP Server for S3 Buckets in AWS

#### This solution deploys an AWS Transfer server that authenticates users via a user/password combination using a Lambda Function. The Lambda function checks a DynamoDB table where the user credentials are stored. If the password is correct, the user is granted SFTP access to a personal folder inside an s3 bucket. Each user will have a dedicated folder and aren't able to access other user's folders inside the bucket. 

#### AWS Resources Deployed: 
- Lambda Function
- DynamoDB table
- AWS Transfer Server
- IAM Permissions 

#### How to use:
1. Download and install AWS SAM CLI. 
2. Inside the project directory, run `sam build` to build the project.
3. Run `sam deploy --guided` to deploy the project.
4. Follow the prompts to deploy the project. (You'll need to specify the S3 bucket to use)
5. Populate the DynamoDB table by adding an item for each user. Example: `{"user": "user1", "password": "password1"}`
