import requests
import json
import random
import time
import math

def up_or_down(visibility):
    probability={80:(["up"]*2)+(["down"]*8),50:(["up"]*5)+(["down"]*5),20:(["up"]*9)+(["down"]*1)}
    opt=""
    if visibility>80:
        opt=random.choice(probability[80])
    elif 50<visibility<80:
        opt=random.choice(probability[50])
    else:
        opt=random.choice(probability[20])
    print(opt)
    if opt=="up":
        return visibility+random.randint(visibility-100-10,100-visibility)
    else:
        return visibility-random.randint(0,min(20,visibility))

#while True:
req=json.loads(requests.get('http://127.0.0.1:8000/info_street').content)
temp_data={d['id']:d['visibility'] for d in req }

random_alter=[random.choice(list(temp_data.keys())) for i in range(math.floor(len(temp_data)/5))]
json_update=[json.dumps({"info":"visibility","id":d,"value":up_or_down(temp_data[d])}) for d in random_alter]

[print(i) for i in json_update]

