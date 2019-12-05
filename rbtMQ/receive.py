#!/usr/bin/env python
import pika
import json
import requests


def callback(ch, method, properties, body):
    body = json.loads(body)

    if body["info"] == "ADD_CAR":
        requests.put("http://192.168.160.237:8000/car/", data = json.dumps({"id":body["id"], "plate":body["plate"]}))
        pass
    elif body["info"] == "REMOVE_CAR":
        requests.delete("http://192.168.160.237:8000/car/", data = json.dumps({"id":body["id"], "plate":body["plate"]}))
        pass


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