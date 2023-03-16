import json
import boto3
import os
import decimal
from botocore.exceptions import ClientError
from pprint import pprint

def lambda_handler(event, context, table=None):
    # either get mocked table from test file or create new one
    if table is None:
        # Initialize dynamodb boto3 object
        dynamodb = boto3.resource('dynamodb')
    
        # Set dynamodb table name variable from env
        ddbTableName = os.environ['databaseName']
        table = dynamodb.Table(ddbTableName)

    # access the table with the update_item function and returns the updated item
    # will retrieve the value of id count. Will then execute the update expression which 
    # will get the visitor count and add one ot it and return the new value
    try:
        ddbResponse = table.update_item(
            Key={"id": "count"},
            UpdateExpression="SET visitor_count = if_not_exists(visitor_count, :start) + :inc",
            ExpressionAttributeValues={
                ":inc": 1,
                ":start": 0,
            },
            ReturnValues="UPDATED_NEW",
        )
    except ClientError as e:
        print("Client error = ", e, " ---- ", e.response['Error']['Message'])
    else:
        # convert into JSON:
        y = json.dumps({ "visitor_count": replace_decimals(ddbResponse["Attributes"]["visitor_count"]) })
        
        apiResponse =  {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Credentials': '*',
                'Content-Type': 'application/json'
            },
            'body': y
        }
        
        # Return api response object
        return apiResponse
    
# function to replace the 'decimal' type numbers
def replace_decimals(obj):
    if isinstance(obj, list):
        for i in range(len(obj)):
            obj[i] = replace_decimals(obj[i])
        return obj
    elif isinstance(obj, dict):
        for k in obj.iterkeys():
            obj[k] = replace_decimals(obj[k])
        return obj
    elif isinstance(obj, decimal.Decimal):
        if obj % 1 == 0:
            return int(obj)
        else:
            return float(obj)
    else:
        return obj