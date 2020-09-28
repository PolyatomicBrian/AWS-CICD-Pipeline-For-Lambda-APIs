import json

def lambda_handler(event, context):
    
    print("Test world")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Test from Lambda!')
    }

