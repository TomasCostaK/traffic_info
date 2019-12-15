#!/usr/bin/env python
import pika
import json
import requests
import time

t = time.time()
queu1 = []
queu2 = []

def callback(ch, method, properties, body):
    global queu1
    global queu2
    global t

    body = json.loads(body)
    if body["type"] in ["insert", "delete"]:
        if body['city'] == 'neighbours':
            queu1.append(body)
        else:
            queu2.append(body)

    elif body["type"] == "visibility":
        msg = json.dumps({"id" : body["id"], "visibility": body["visibility"], "city":body["city"]})
        print(msg)
        #requests.put("http://192.168.160.237:8000/visibility/", data = msg, headers={"Content-Type":"text/plain"})
    elif body["type"] == "roadblock_down":
        msg = json.dumps({"id" : body["id"], "city":body["city"]})
        print(msg)
        #requests.delete("http://192.168.160.237:8000/roadblock/", data = msg, headers={"Content-Type":"text/plain"})
    elif body["type"] == "roadblock_up":
        msg = json.dumps({"id" : body["id"], "city":body["city"]})
        print(msg)
        #requests.put("http://192.168.160.237:8000/roadblock/", data = msg, headers={"Content-Type":"text/plain"})
    elif body["type"] == "police_down":
        msg = json.dumps({"id" : body["id"], "city":body["city"]})
        print(msg)
        #requests.delete("http://192.168.160.237:8000/police/", data = msg, headers={"Content-Type":"text/plain"})
    elif body["type"] == "police_up":
        msg = json.dumps({"id" : body["id"], "city":body["city"]})
        print(msg)
        #requests.put("http://192.168.160.237:8000/police/", data = msg, headers={"Content-Type":"text/plain"})

    
    if len(queu1) == 100:    #SEND CARS IN BULK
        #print(time.time() - t)

        msg = json.dumps({"type":"various_cars", "city": "aaaa", "data":queu1})
        print(msg)
        #requests.put("http://192.168.160.237:8000/car/", data = msg, headers={"Content-Type":"text/plain"})

        queu1 = []
        t = time.time()

    if len(queu2) == 100:
        #print(time.time() - t)

        msg = json.dumps({"type":"various_cars","city": "bbbb", "data":queu2})
        print(msg)
        #requests.put("http://192.168.160.237:8000/car/", data = msg, headers={"Content-Type":"text/plain"})

        queu2 = []
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