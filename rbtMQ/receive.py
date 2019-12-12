#!/usr/bin/env python
import pika
import json
import requests
import time

t = time.time()
queu = []

def callback(ch, method, properties, body):
    global queu

    body = json.loads(body)
    if body["type"] in ["insert", "delete"]:
        queu.append(body)
    elif body["type"] == "visibility":
        msg = json.dumps({"id" : body["id"], "visibility": body["visibility"]})
        print(msg)
        #requests.put("http://192.168.160.237:8000/visibility/", data = msg, headers={"Content-Type":"text/plain"})
    elif body["type"] == "roadblock_down":
        msg = json.dumps({"id" : body["id"]})
        print(msg)
        #requests.delete("http://192.168.160.237:8000/roadblock/", data = msg, headers={"Content-Type":"text/plain"})
    elif body["type"] == "roadblock_up":
        msg = json.dumps({"id" : body["id"]})
        print(msg)
        #requests.put("http://192.168.160.237:8000/roadblock/", data = msg, headers={"Content-Type":"text/plain"})
    elif body["type"] == "police_down":
        msg = json.dumps({"id" : body["id"]})
        print(msg)
        #requests.delete("http://192.168.160.237:8000/police/", data = msg, headers={"Content-Type":"text/plain"})
    elif body["type"] == "police_up":
        msg = json.dumps({"id" : body["id"]})
        print(msg)
        #requests.put("http://192.168.160.237:8000/police/", data = msg, headers={"Content-Type":"text/plain"})

    
    if len(queu) == 100:    #SEND CARS IN BULK
        global t
        print(time.time() - t)

        msg = json.dumps({"type":"various_cars", "data":queu})
        #print(msg)
        #requests.put("http://192.168.160.237:8000/car/", data = msg, headers={"Content-Type":"text/plain"})

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