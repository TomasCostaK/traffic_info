#!/usr/bin/env python
import pika
import json
import time
from random import randint, choice, gauss
import os
import sys
import string
import requests
import math


#MAKE CONNECTION
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
#SET QUEUE
channel.queue_declare(queue='cars')


class Sensor:
    def __init__(self, neighboursFile):

        #INITIALIZE DATA
        f = open(neighboursFile, "r")
        self.neighbours = json.loads(f.read())
        f.close()
        self.number_of_trechos = len(self.neighbours)

        self.actual_info = {}
        for i in range(1,self.number_of_trechos+1):
            self.actual_info[i] = []


    def add(self,trecho, plate):
        msg = json.dumps({"type": "insert", "id" : trecho, "plate":plate })
        #print(msg)
        channel.basic_publish(exchange='', routing_key='cars', body=msg)

    def remove(self,trecho, plate):
        msg = json.dumps({"type": "delete", "id" : trecho, "plate":plate })
        #print(msg)
        channel.basic_publish(exchange='', routing_key='cars', body=msg)

    def printInfo(self):
        os.system('clear')
        n = 0
        for trecho in self.actual_info:
            if 'TESTE1' in self.actual_info[trecho]:
                n = trecho

            if len(self.actual_info[trecho]) > 170:
                print("Trecho %-2d : %-4d" % (trecho, len(self.actual_info[trecho])))

        print('--------------------------------')

        for trecho in self.actual_info:
            if len(self.actual_info[trecho]) < 50:
                print("Trecho %-2d : %-4d" % (trecho, len(self.actual_info[trecho])))

        print('TESTE1 in ' + str(n))


    def forceTraffic(self):
        trecho = randint(1, self.number_of_trechos)
        while len(self.actual_info[trecho]) < 180:
            plate = ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(6))
            self.actual_info[trecho].append(plate)
            self.add(trecho, plate)
            time.sleep(0.01)


    def reduceTraffic(self):
        highTraffic = {}
        for trecho in self.actual_info:
            if len(self.actual_info[trecho]) >= 170:
                highTraffic[trecho] = len(self.actual_info[trecho])

        mostCars = [i[0] for i in sorted(highTraffic.items(), key= lambda e : (e[1], e[0]), reverse=True)]

        for i in range(len(mostCars)):
            if i == 5 :
                break
            
            trecho = mostCars[i]

            while len(self.actual_info[trecho]) > 100:
                trechoOut = self.neighbours[str(trecho)][randint(0, len(self.neighbours[str(trecho)])-1)]
                plateOut = self.actual_info[trecho][randint(0, len(self.actual_info[trecho])-1)]

                disapear = randint(0,1) == 0
                if disapear:
                    if plateOut != 'TESTE1':
                        self.actual_info[trecho].remove(plateOut)
                        self.remove(trecho, plateOut)
                else:
                    self.actual_info[trecho].remove(plateOut)
                    self.remove(trecho, plateOut)

                    self.actual_info[trechoOut].append(plateOut)
                    self.add(trechoOut, plateOut)
                time.sleep(0.01)

    def populate(self):
        self.add(1, 'TESTE1')
        self.actual_info[1].append('TESTE1')

        for i in range(randint(self.number_of_trechos*50, self.number_of_trechos * 150)):
            trecho = randint(1, self.number_of_trechos)
            plate = ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(6))

            self.actual_info[trecho].append(plate)
            self.add(trecho, plate)
    
    def visibility(self):
        req=json.loads(requests.get('http://192.168.160.237:8000/info_street').content)
        temp_data={d['id']:d['visibility'] for d in req }

        random_alter=[choice(list(temp_data.keys())) for i in range(math.floor(len(temp_data)/5))]
        for d in random_alter:
            temp_data[d]=min(100,max(0,math.ceil(gauss(60,25))))
            
        #[print(f"ID- {d} Value-{temp_data[d]}") for d in temp_data]
        [channel.basic_publish(exchange='', routing_key='cars', body=json.dumps({"type":"visibility", "id":d, "value": temp_data[d]} )) for d in temp_data]

    
    def roadBlock(self,req):    
        data={d['id']:True if d['transit_type']=='Blocked' else False for d in req }

        # Generating positive values to go negative and negative to go positive
        data_positive=[d for d in data if data[d]==True]
        data_negative=[d for d in data if data[d]==False]

        if len(data_positive)!=0:
            random_data_positive=[choice(data_positive) for i in range(min(5,len(data_positive)))]
            json_update_true=[json.dumps({"type":"roadblock_down","id":d}) for d in random_data_positive]
            [channel.basic_publish(exchange='', routing_key='cars', body=i) for i in json_update_true]

        if len(data_negative)!=0:
            random_data_negative=[choice(data_negative) for i in range(min(2,len(data_negative)))]
            json_update_false=[json.dumps({"type":"roadblock_up","id":d}) for d in random_data_negative]
            [channel.basic_publish(exchange='', routing_key='cars', body=i) for i in json_update_false]


    def police(self, req):
        data={d['id']:d['police'] for d in req}

        # Generating positive values to go negative and negative to go positive
        data_positive=[d for d in data if data[d]==True]
        data_negative=[d for d in data if data[d]==False]
        if len(data_positive)!=0:
            random_data_positive=[choice(data_positive) for i in range(min(5,len(data_positive)))]
            json_update_true=[json.dumps({"type":"police_down","id":d}) for d in random_data_positive]
            [channel.basic_publish(exchange='', routing_key='cars', body=i) for i in json_update_true]

        if len(data_negative)!=0:
            random_data_negative=[choice(data_negative) for i in range(min(2,len(data_negative)))]
            json_update_false=[json.dumps({"type":"police_up","id":d}) for d in random_data_negative]
            [channel.basic_publish(exchange='', routing_key='cars', body=i) for i in json_update_false]



    def startSensor(self):

        #SENSOR
        i = 1   #just to debug
        while True:
            if i % 200 == 0:
                self.printInfo()
                self.visibility()
                pass
            if i % 500 == 0:
                req=json.loads(requests.get('http://192.168.160.237:8000/info_street').content)

                self.forceTraffic() 
                self.roadBlock(req)   
                self.police(req)   
            if i % 2000 == 0:
                self.reduceTraffic()

            trecho = randint(1,self.number_of_trechos)
            trechoOut = self.neighbours[str(trecho)][randint(0, len(self.neighbours[str(trecho)])-1)]

            if len(self.actual_info[trecho]) != 0:
                plateOut = self.actual_info[trecho][randint(0, len(self.actual_info[trecho])-1)]
                self.actual_info[trecho].remove(plateOut)
                self.actual_info[trechoOut].append(plateOut)

                self.remove(trecho, plateOut)
                self.add(trechoOut, plateOut)
            
            i+=1
            if i == 1000000:
                i = 0
            time.sleep(0.01)


sensor = Sensor(sys.argv[1])
print("populating")
sensor.populate()
sensor.startSensor()

connection.close()
