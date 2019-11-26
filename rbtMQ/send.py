#!/usr/bin/env python
import pika
import json
import time
from random import randint
import os

#MAKE CONNECTION
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#SET QUEUE
channel.queue_declare(queue='virtual_sensors')

#INITIALIZE DATA
f = open("neighbours.txt", "r")
neighbours = json.loads(f.read())
f.close()
number_of_trechos = len(neighbours)

#Keep track of information so that don't remove car from empty street
actual_info = {}
for i in range(number_of_trechos):
    actual_info[i] = randint(5,20)  #trecho begins with 5<cars>20

def printInfo():
    os.system('clear')
    for trecho in actual_info:
        print("Trecho %-2d : %-4d" % (trecho, actual_info[trecho]))

#SENSOR
while True:
    printInfo()

    trecho = randint(0,number_of_trechos-1)
    trechoOut = neighbours[str(trecho)][randint(0, len(neighbours[str(trecho)])-1)]
    #carOut = randint(0,1) == 1

    # if carOut and actual_info[trecho] != 0:
    #     info = "REMOVE_CAR"
    #     actual_info[trecho] -= 1
    # else:
    #     info = "ADD_CAR"
    #     actual_info[trecho] += 1

    if actual_info[trecho] != 0:
        actual_info[trecho] -= 1
        msg = json.dumps({"id" : trecho, "info": "REMOVE_CAR"})
        channel.basic_publish(exchange='', routing_key='virtual_sensors', body=msg)     #CAR LEFT

        actual_info[trechoOut] += 1
        msg = json.dumps({"id" : trechoOut, "info": "ADD_CAR"})
        channel.basic_publish(exchange='', routing_key='virtual_sensors', body=msg)     #CAR JOINED
    
    
    time.sleep(0.05)

connection.close()


