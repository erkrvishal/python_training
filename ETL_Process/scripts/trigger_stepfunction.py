import json
import boto3

def lambda_handler(event, context):

    print(event)
    client = boto3.client('stepfunctions')

    execution_input = {
        "bucket": event['Records'][0]['s3']['bucket']['name'],
        "key": event['Records'][0]['s3']['object']['key']
    }
    # If we have to convert JSON to JSON String --> json.dunps()
    # If we have to convert JSON String to JSON --> json.loads() 
    response = client.start_execution(
        stateMachineArn='', #Place the step function arn
        input=json.dumps(execution_input)
    )
    print(f"Execution ARN: {response['executionArn']}")
