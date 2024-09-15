import json
import boto3

client = boto3.client('lambda')

def lambda_handler(event, context):
    inputForInvoker = {'CustomerId' : 'C2626', 'CustomerName' : 'John Doe'}
    
    response = client.invoke(
        FunctionName="arn:aws:lambda:ap-south-1:339713133450:function:LambdaToInvoke",
        InvocationType='RequestResponse', # Event -> Async, DryRun RequestResponse -> RequestResponse
        Payload=json.dumps(inputForInvoker)
    )
    
    responseJson = json.loads(response['Payload'])
    
    print(f"Response from Invoked Lambda: {responseJson}")
    
    return responseJson
