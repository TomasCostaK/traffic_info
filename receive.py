#!/usr/bin/env python
import pika
import json

def addCar(id):
    #ADD TO DB
    print("ADD    CAR IN TRECHO " + str(id))

def remCar(id):
    #SUB TO DB
    print("REMOVE CAR IN TRECHO " + str(id))


def callback(ch, method, properties, body):
    body = json.loads(body)

    if body["info"] == "ADD_CAR":
        addCar(body["id"])
    elif body["info"] == "REMOVE_CAR":
        remCar(body["id"])


#MAKE CONNECTION
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#SET QUEUE
channel.queue_declare(queue='virtual_sensors')

channel.basic_consume(
    queue='virtual_sensors', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

#START CONSUMING
channel.start_consuming()