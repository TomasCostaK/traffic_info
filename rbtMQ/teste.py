import json
import requests

requests.put("http://192.168.160.237:8000/car/", data = json.dumps({"id":10, "plate":"TESTE2"}))