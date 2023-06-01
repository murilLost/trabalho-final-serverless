import json
from baseDAO import BaseDAO
from sqsHandler import SqsHandler

dao = BaseDAO('eventos-pizzaria')

sqs = SqsHandler('https://sqs.us-east-1.amazonaws.com/746997494603/espera-entrega')

def sqsHandler(event, context):
    print("event: {}".format(json.dumps(event)))
    item=event["detail"]
    sqs.send("detail: {}".format(json.dumps(item)))
    
    return True
    
def dynamoHandler(event, context):
    print("event: {}".format(json.dumps(event)))
    item=event["detail"]
    item["time"]=event["time"]
    dao.put_item(item)
    
    return True
    
def processSqs(event, context):
    while(True):
        response = sqs.getMessage(10)
    
        if('Messages' not in response):
            break
    
        if(len(response['Messages']) == 0):
            break
    
        for msg in response['Messages']:
            print(msg["Body"])
        
            sqs.deleteMessage(msg['ReceiptHandle'])