#!/usr/bin/env python
import pika
import json
import requests
import time

t = time.time()
queu = []

def sendToServer():
    msg = json.dumps({"type":"various_cars", "data":queu})
    #requests.put("http://192.168.160.237:8000/car/", data = msg)

def callback(ch, method, properties, body):
    global queu

    body = json.loads(body)
    if body["type"] in ["insert", "delete"]:
        queu.append(body)
    else:
        print(body)
    
    '''if body["info"] == "ADD_CAR":
        requests.put("http://192.168.160.237:8000/car/", data = json.dumps({"id":body["id"], "plate":body["plate"]}))
        pass
    elif body["info"] == "REMOVE_CAR":
        requests.delete("http://192.168.160.237:8000/car/", data = json.dumps({"id":body["id"], "plate":body["plate"]}))
        pass
        '''
    if len(queu) == 100:
        global t
        #print(time.time() - t)

        sendToServer()
        queu = []
        t = time.time()



#MAKE CONNECTION
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#SET QUEUE
channel.queue_declare(queue='cars')

channel.basic_consume(
    queue='cars', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

#START CONSUMING
channel.start_consuming()