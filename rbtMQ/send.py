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

#INITIALIZE DATA
f = open(sys.argv[1], "r")
neighbours = json.loads(f.read())
f.close()
number_of_trechos = len(neighbours)

actual_info = {}
for i in range(1,number_of_trechos+1):
    actual_info[i] = []


def add(trecho, plate):
    msg = json.dumps({"info": "ADD_CAR", "id" : trecho, "plate":plate })
    #print(msg)
    channel.basic_publish(exchange='', routing_key='cars', body=msg)

def remove(trecho, plate):
    msg = json.dumps({"info": "REMOVE_CAR", "id" : trecho, "plate":plate })
    #print(msg)
    channel.basic_publish(exchange='', routing_key='cars', body=msg)

def printInfo():
    os.system('clear')
    n = 0
    for trecho in actual_info:
        if 'TESTE1' in actual_info[trecho]:
            n = trecho

        if len(actual_info[trecho]) > 200:
            print("Trecho %-2d : %-4d" % (trecho, len(actual_info[trecho])))
    
    print('--------------------------------')

    for trecho in actual_info:
        if len(actual_info[trecho]) < 100:
            print("Trecho %-2d : %-4d" % (trecho, len(actual_info[trecho])))
    
    print('TESTE1 in ' + str(n))


def generateSome(actual_info, nTrechos):
    #generate 20-50 cars per trecho
    for i in range(randint(nTrechos*20, nTrechos * 50)):
        trecho = randint(1, nTrechos)
        plate = ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(6))
        
        actual_info[trecho].append(plate)
        add(trecho, plate)

def removeSome(actual_info, nTrechos):
    #remove 20-50 cars per trecho
    for i in range(randint(nTrechos*20, nTrechos*50)):
        trecho = randint(1, nTrechos)
        if actual_info[trecho] != []:

            plate = choice(actual_info[trecho])

            if plate != 'TESTE1':
                actual_info[trecho].remove(plate)
                remove(trecho, plate)

def forceTraffic(actual_info, nTrechos):
    trecho = randint(1, nTrechos)
    #print(str(trecho) + ' tinha ' + str(len(actual_info[trecho])))
    while len(actual_info[trecho]) < 210:
        plate = ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(6))
        actual_info[trecho].append(plate)
        add(trecho, plate)
    
    #print(str(trecho) + ' ficou ' + str(len(actual_info[trecho])))


def reduceTraffic(actual_info, nTrechos):
    highTraffic = {}
    for trecho in actual_info:
        if len(actual_info[trecho]) >= 200:
            highTraffic[trecho] = len(actual_info[trecho])
    
    mostCars = [i[0] for i in sorted(highTraffic.items(), key= lambda e : (e[1], e[0]), reverse=True)]
    
    for i in range(len(mostCars)):

        if i == 5 :
            break
        
        trecho = mostCars[i]
        

        while len(actual_info[trecho]) > 100:
            trechoOut = neighbours[str(trecho)][randint(0, len(neighbours[str(trecho)])-1)]
            plateOut = actual_info[trecho][randint(0, len(actual_info[trecho])-1)]

            disapear = randint(0,1) == 0
            if disapear:
                if plateOut != 'TESTE1':
                    actual_info[trecho].remove(plateOut)
                    remove(trecho, plateOut)
            else:
                actual_info[trecho].remove(plateOut)
                remove(trecho, plateOut)

                actual_info[trechoOut].append(plateOut)
                add(trechoOut, plateOut)
        

def trechosUnder100(actual_info):
    c = 0
    for trecho in actual_info:
        if len(actual_info[trecho]) < 100:
            c += 1
    return c

def trechosOver200(actual_info):
    c = 0
    for trecho in actual_info:
        if len(actual_info[trecho]) > 200:
            c += 1
    return c


add(1, 'TESTE1')
actual_info[1].append('TESTE1')

generateSome(actual_info, number_of_trechos)
generateSome(actual_info, number_of_trechos)
generateSome(actual_info, number_of_trechos)
generateSome(actual_info, number_of_trechos)

#SENSOR
i = 1   #just to debug
while True:
    if i % 200 == 0:
        printInfo()
    if i % 500 == 0:
        forceTraffic(actual_info, number_of_trechos)
    '''if i % 1000 == 0:
        if trechosUnder100(actual_info) > number_of_trechos / 2:
            removeCars = randint(0,3) == 0

        elif trechosOver200(actual_info) > number_of_trechos / 2:
            removeCars = randint(0,3) in [0,1,2]
            
        else:
            removeCars = randint(0,1) == 0

        if removeCars:
            removeSome(actual_info, number_of_trechos)
        else:
            generateSome(actual_info, number_of_trechos)'''
    
    if i % 2000 == 0:
        reduceTraffic(actual_info, number_of_trechos)
       
    

    trecho = randint(1,number_of_trechos)
    trechoOut = neighbours[str(trecho)][randint(0, len(neighbours[str(trecho)])-1)]

    if len(actual_info[trecho]) != 0:
        plateOut = actual_info[trecho][randint(0, len(actual_info[trecho])-1)]
        actual_info[trecho].remove(plateOut)
        actual_info[trechoOut].append(plateOut)

        remove(trecho, plateOut)
        add(trechoOut, plateOut)
       
    i+=1
    if i == 1000000:
        i = 0
    #time.sleep(0.01)




connection.close()


