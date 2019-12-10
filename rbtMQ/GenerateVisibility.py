import requests
import json
import random
import time
import math


req=json.loads(requests.get('http://192.168.160.237:8000/info_street').content)
temp_data={d['id']:d['visibility'] for d in req }
while True:
    random_alter=[random.choice(list(temp_data.keys())) for i in range(math.floor(len(temp_data)/5))]
    for d in random_alter:
        temp_data[d]=min(100,max(0,math.ceil(random.gauss(60,25))))

    [print(f"ID- {d} Value-{temp_data[d]}") for d in temp_data]
    time.sleep(2)