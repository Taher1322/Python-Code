import RPi.GPIO as GPIO
from time import time, sleep
from urllib.request import urlopen
import sys

#GPIO SETUP
channel = 17  #physical pin 11 on raspberry pi 
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

WRITE_API = "UE6UU8JFDCIHLVKT" # Replace your ThingSpeak API key here
BASE_URL = "https://api.thingspeak.com/update?api_key={}".format(WRITE_API)


def my_callback(channel):
        if (GPIO.input(channel)==1):
                print("Movement Detected!")
                value = 1;
                thingspeakHttp = BASE_URL + "&field1={:.2f}".format(value)
                print(thingspeakHttp)
            
                conn = urlopen(thingspeakHttp)
                print("Response: {}".format(conn.read()))
                conn.close()
    
        elif (GPIO.input(channel)==0):
                print("No Movement Detected!")
                value = 0;
                thingspeakHttp = BASE_URL + "&field1={:.2f}".format(value)
                print(thingspeakHttp)
            
                conn = urlopen(thingspeakHttp)
                print("Response: {}".format(conn.read()))
                conn.close()
    

GPIO.add_event_detect(channel, GPIO.BOTH, callback=my_callback, bouncetime=500)  

# infinite loop
while True:
        sleep(1)