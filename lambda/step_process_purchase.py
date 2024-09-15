import json
import datetime

def lambda_handler(event, context):
    
    # Input example
    # {"TransactionType" : 'PURCHASE'}
    
    print("Received message from Step Function: ", event)
    
    # Construct the response
    response = {
        'TransactionType': event['TransactionType'],
        'TransactionStatus': 'SUCCESS',
        'TransactionDateTime': str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        'Message': 'Purchase transaction processed successfully'
    }
    
    return response
    