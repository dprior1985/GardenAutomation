import urllib2
import json
import RPi.GPIO as GPIO
import time
import MySQLdb
import datetime
import os
import sys

sys.path.append('/home/pi/Desktop/GardenAutomation/modules')

import lightsensor
import openrelay
import TemperatureSenor
import WeatherAPI


#GPIO PINS SETUP
GPIO.setmode(GPIO.BOARD)


#temperature1 =	TemperatureSenor.Sensor("28-0115524404ff")
temperature2 =	TemperatureSenor.Sensor("28-031553a54dff")
#temperature3 =	TemperatureSenor.Sensor("28-031553aaf4ff")
#temperature4 =	TemperatureSenor.Sensor("28-031553aca3ff")
temperature5 =	TemperatureSenor.Sensor("28-031553b046ff")

#print (temperature1)
print (temperature2)
#print (temperature3)
#print (temperature4)
#print (temperature5)


print("33 start")
light1 = lightsensor.RCtime(33)
print(light1)
#light2 = lightsensor.RCtime(36)
#print(light2)
	


openrelay.Run(10)