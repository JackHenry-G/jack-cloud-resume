import boto3 
import json 

def lambda_handler( event, context ):    
    #setup emails to and from
    from_address = 'portfolio_sender_jackHG@outlook.com'
    to_address = 'jack_HG@outlook.com'
    
    name = event['name']
    return_email = event['email']
    subject = event['subject']
    message = event['message']
    
    
    
    #load the ses client 
    client = boto3.client('ses')
    
    response = client.send_email(
        Source= from_address, 
        Destination={
            'ToAddresses':[
                    to_address
                ]            
        }, 
        Message={
            'Subject': {
                'Data': subject
            }, 
            'Body':{
                'Text':{
                    'Data': 'Hi Jack,\n\nMy name is ' + name +  ' I am contacting you via your portfolio webpage hosted on AWS. Please return me an email at ' + return_email + '.\n\n' + message 
                }
            }
        }
    )
    
    return {
        'status': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Credentials': '*',
            'Content-Type': 'application/json'
        },
        'body': json.dumps( response ) 
    }