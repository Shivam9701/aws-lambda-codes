import json


def lambda_handler(event, context):
    # Parse query string parameters
    transactionId = event["queryStringParameters"]["transactionId"]
    transactionType = event["queryStringParameters"]["type"]
    transactionAmount = event["queryStringParameters"]["amount"]

    # Print the query string parameters
    print(f"Transaction ID: {transactionId}")
    print(f"Transaction Type: {transactionType}")
    print(f"Transaction Amount: {transactionAmount}")

    # Prepare the response
    responseBody = {
        "transactionId": transactionId,
        "transactionType": transactionType,
        "transactionAmount": transactionAmount,
    }
    
    responseObj = {
        "statusCode": 200,
        "body": json.dumps(responseBody),
        "headers": {
            "Content-Type": "application/json",
        },
    }
    
    return responseObj
    
    
