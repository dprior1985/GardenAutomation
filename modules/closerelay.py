import RPi.GPIO as GPIO
import time
from datetime import datetime 
import os

now = datetime.now()

relay = 38




def Run(sec):

	try:
		GPIO.output(relay,GPIO.HIGH)
		print("Replay Closed")
		print(datetime.now())
	
	except:
		print ("Water pump error")
		GPIO.output(relay,GPIO.HIGH)
		
