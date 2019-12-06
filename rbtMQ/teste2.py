#!/usr/bin/env python
import pika
import json
import time
from random import randint, choice
import os
import sys
import string

#MAKE CONNECTION
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
#SET QUEUE
channel.queue_declare(queue='cars')

def add(trecho, plate):
    msg = json.dumps({"info": "ADD_CAR", "id" : trecho, "plate":plate })
    print(msg)
    channel.basic_publish(exchange='', routing_key='cars', body=msg)

def remove(trecho, plate):
    msg = json.dumps({"info": "REMOVE_CAR", "id" : trecho, "plate":plate })
    #print(msg)
    channel.basic_publish(exchange='', routing_key='cars', body=msg)

trecho = randint(1, 5)

for i in range(100):
    plate = ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(6))
    
    add(trecho, plate)