import json
import boto3
import time

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('table_name') #replace 'table_name' with the name of your DynamoDB table

def lambda_handler(event, context):
    print (event)
    #receives data from REST API
    downTime = event['downTime']
    upTime = event['upTime']
    maxTemp = event['maxTemp']
    
    #converts unix time into a more readable format
    dT_formatted = time.strftime('%B %-d, %Y %H:%M:%S', time.localtime(int(downTime)))
    uT_formatted = time.strftime('%B %-d, %Y %H:%M:%S', time.localtime(int(upTime)))
    
    #writing the data to a DynamoDB table
    table.put_item(
            Item={
                'downTime':dT_formatted,
                'upTime':uT_formatted,
                'maxTemp':maxTemp,
            }
        )
    
    #creating and sending SNS message
    sns_client = boto3.client('sns')
    msg = "Out at:\n" + dT_formatted + "\n\nBack on:\n" + uT_formatted + "\n\nHighest temperature: " + maxTemp + " degrees Fahrenheit"
    sns_client.publish(TopicArn='snsARN',Message = msg, Subject = 'Power Outage Report') #replace 'snsARN' with the Amazon Resource Name of your SNS topic
    return 'added record successfully'
