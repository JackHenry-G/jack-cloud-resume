from UpdateVisitorCount import lambda_handler
from pprint import pprint
import unittest
import boto3 # AWS SDK for Python
from botocore.exceptions import ClientError
from moto import * # Moto is a library that allows your tests to easily mock out AWS Services.

@mock_dynamodb
class TestDatabaseFunctions(unittest.TestCase):

    def setUp(self):
        """
        Create database resource and mock dyanmodb table.

        """
        self.dynamodb = boto3.resource('dynamodb', region_name='eu-west-2')
        # Create the DynamoDB table.
        self.count_table = self.dynamodb.create_table(
            TableName='VisitorCountCloudChallenge',
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        
    def tearDown(self):
        """
        Delete database resource and mock table
        """
        self.dynamodb=None
    
    def test_updateVisitorCounter(self):
        """
        Test if our mock table is ready
        """
        self.assertEqual('VisitorCountCloudChallenge', self.count_table.name) # check if the table name is right
        #self.assertEqual('ACTIVE', self.count_table['TableDescription']['TableStatus'])


        event = {}
        context = {}
        

        # no data in current database, so must make a new value and set it to 1 (first visitor to webpage)
        self.assertEqual(lambda_handler(event, context, table=self.count_table), {'statusCode': 200, 'headers': {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': '*', 'Access-Control-Allow-Credentials': '*', 'Content-Type': 'application/json'}, 'body': '{"visitor_count": 1}'}, "Incorrect resopnse for updating database with no records in")

        # second visit to webpage, so 1 + 1 = 2
        self.assertEqual(lambda_handler(event, context, table=self.count_table), {'statusCode': 200, 'headers': {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': '*', 'Access-Control-Allow-Credentials': '*', 'Content-Type': 'application/json'}, 'body': '{"visitor_count": 2}'}, "Incorrect resopnse for updating database with existing records")


if __name__ == '__main__':
    unittest.main()