import requests
import json
import random
import time
while True:
    req=json.loads(requests.get('http://192.168.160.237:8000/info_street').content)
    data={d['id']:d['police'] for d in req}
    time.sleep(5)
    # Generating positive values to go negative and negative to go positive
    data_positive=[d for d in data if data[d]==True] # There is police
    data_negative=[d for d in data if data[d]==False] # There is no police
    if len(data_positive)!=0:
        random_data_positive=[random.choice(data_positive) for i in range(min(5,len(data_positive)))]
    if len(data_negative)!=0:
        random_data_negative=[random.choice(data_negative) for i in range(min(2,len(data_negative)))]

    json_update_true=[json.dumps({"info":"police_down","id":d}) for d in random_data_positive]
    json_update_false=[json.dumps({"info":"police_up","id":d}) for d in random_data_negative]

for i in json_update_true:
    r=requests.delete("http://192.168.160.237:8000/roadblock/",data=json.dumps(i),headers={"Content-Type":"text/plain"})

for f in json_update_false:
    r=requests.put("http://192.168.160.237:8000/roadblock/",data=json.dumps(f),headers= {"Content-Type":"text/plain"})
