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
number_of_trechos = 10

#Keep track of information so that don't remove car from empty street
actual_info = {}
for i in range(number_of_trechos):
    actual_info[i] = randint(5,20)  #trecho begins with 5<cars>20

def printInfo():
    os.system('clear')
    for trecho in actual_info:
        print("Trecho %-2d : %-4d" % (trecho, actual_info[trecho]))

while True:
    printInfo()

    trecho = randint(0,number_of_trechos-1)
    carOut = randint(0,1) == 1

    if carOut and actual_info[trecho] != 0:
        info = "REMOVE_CAR"
        actual_info[trecho] -= 1
    else:
        info = "ADD_CAR"
        actual_info[trecho] += 1
    
    msg = json.dumps({"id" : trecho, "info": info})
    channel.basic_publish(exchange='', routing_key='virtual_sensors', body=msg)
    time.sleep(0.1)

connection.close()


