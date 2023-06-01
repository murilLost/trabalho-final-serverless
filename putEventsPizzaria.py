import boto3
import json
import datetime

import random

clientes = ['rafael','maria','teresa', 'tatiane', 'murilo']
statusPossiveis = ['pedido feito','montando', 'no forno','saiu do forno', 'embalando','pronto']

peeker = random.SystemRandom()

eventBridge = boto3.client('events')

def put_events(eventBus, source, detailType, detail):
    response = eventBridge.put_events(
        Entries=[
            {
                'Time': datetime.datetime.now(),
                'Source': source,
                'DetailType': detailType,
                'Detail': json.dumps(detail),
                'EventBusName': eventBus,
            }
        ]
    )
    
def makeEvent(status, pedido, cliente):
    eventBus="pizzaria"
    source = "com.pizza.status"
    detailType = "Alteracao Pizza"
    detail = {
      "status": status,
      "pedido": pedido,
      "cliente": cliente
    }
    put_events(eventBus, source, detailType, detail)

for i in range(10):
   cliente = peeker.choice(clientes)
   
   for status in statusPossiveis:
       makeEvent(status, str(i), cliente)