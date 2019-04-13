import Adafruit_DHT
import time
import requests
import json
import RPi.GPIO as s




s.setwarnings(False)
s.setmode(s.BCM)
s.setup(4,s.OUT)

while 1:
            humidity,temperature=Adafruit_DHT.read_retry(11,4)
            print(str(humidity),str(temperature))
            x=str(humidity)
            y=str(temperature)
            print("Posting")
            url1=requests.post("https://api.thingspeak.com/update?api_key=6F8N37PF3YAMAT1U&field1="+x+"&field2"+y)
            print("getting")
            url=requests.get("https://api.thingspeak.com/channels/591630/feeds.json?api_key=25H4GYI2KAYOAIIN&results=2")
            res=url.json()
            print(res)
            a=res['feeds'][0]['field1']
            b=res['feeds'][0]['field2']
            print(a)
            print(b)
