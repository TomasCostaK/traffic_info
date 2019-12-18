import requests
import json
import random
import time
#while True:
req=json.loads(requests.get('http://192.168.160.237:8000/info_street').content)
data={d['id']:True if d['transit_type']=='Blocked' else False for d in req }
time.sleep(5)
# Generating positive values to go negative and negative to go positive
data_positive=[d for d in data if data[d]==True] # Blocked
data_negative=[d for d in data if data[d]==False] # Not Blocked
random_data_positive=[]
random_data_negative=[]
if len(data_positive)!=0:
    for i in range(min(5,len(data_positive))):
        choice=random.choice(data_positive)
        if choice not in random_data_positive:
            random_data_positive.append(choice)

if len(data_negative)!=0:
    for i in range(min(2,len(data_negative))):
        choice=random.choice(data_negative)
        if choice not in random_data_negative:
            random_data_negative.append(choice)

json_update_true=[{"info":"roadblock_down","id":d} for d in random_data_positive] # Blocked
json_update_false=[{"info":"roadblock_up","id":d} for d in random_data_negative] # Not blocked

for i in json_update_true:
    r=requests.delete("http://192.168.160.237:8000/roadblock/",data=json.dumps(i),headers={"Content-Type":"text/plain"})

  
for f in json_update_false:
    r=requests.put("http://192.168.160.237:8000/roadblock/",data=json.dumps(f),headers= {"Content-Type":"text/plain"})
