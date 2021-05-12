from time import time, sleep
from urllib.request import urlopen
import sys

WRITE_API = "XXXX" # Replace your ThingSpeak API key here
BASE_URL = "https://api.thingspeak.com/update?api_key={}".format(WRITE_API)


try:
    while True:
        #Sending some static values in the field of Thingspeak platform      
        humidity = 70.54
        temperature = 27.65
        thingspeakHttp = BASE_URL + "&field1={:.2f}&field2={:.2f}".format(temperature, humidity)
        print(thingspeakHttp)
            
        conn = urlopen(thingspeakHttp)
        print("Response: {}".format(conn.read()))
        conn.close()
    
        sleep(5)
            
except KeyboardInterrupt:
    conn.close()
