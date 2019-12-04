import requests
import json
import random
import time
while True:
    req=json.loads(requests.get('http://127.0.0.1:8080/info_street').content)