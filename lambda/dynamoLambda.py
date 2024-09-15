import json


def lambda_handler(event, context):
    
    try:
        #Iterate over each record in the event
        print('---------------------------------')
        for record in event['Records']:
            
            if record['eventName'] == 'INSERT':
                handle_insert(record)
            elif record['eventName'] == 'MODIFY':
                handle_modify(record)
            elif record['eventName'] == 'REMOVE':
                handle_remove(record)
        
        print('---------------------------------')
        
    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Internal Server Error')
        }

def handle_insert(record):
    print(f"Inserting record: {record['dynamodb']['NewImage']}")
    
    