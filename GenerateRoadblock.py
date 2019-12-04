import requests
import json
import random
import time
while True:
    req=json.loads(requests.get('http://127.0.0.1:8080/info_street').content)
    data={d['id']:True if d['transit_type']=='Blocked' else False for d in req }
    time.sleep(5)
    # Generating positive values to go negative and negative to go positive
    data_positive=[d for d in data if data[d]==True]
    data_negative=[d for d in data if data[d]==False]

    if len(data_positive)!=0:
        random_data_positive=[random.choice(data_positive) for i in range(min(5,len(data_positive)))]
    if len(data_negative)!=0:
        random_data_negative=[random.choice(data_negative) for i in range(min(2,len(data_negative)))]

    json_update_true=[json.dumps({"info":"roadblock_down","id":d}) for d in random_data_positive]
    json_update_false=[json.dumps({"info":"roadblock_up","id":d}) for d in random_data_negative]
    [print(i) for i in json_update_true]
    [print(f) for f in json_update_false]