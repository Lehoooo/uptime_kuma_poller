import requests
import time
import json

with open("config.json", "r") as f:
    config = json.load(f)
    url = config["url"]

while True:
    try:
        print("sending")
        requests.get(url)
        print("sent")
        time.sleep(10)
    except Exception as e:
        print(e)
        print("error")
