import RPi.GPIO as GPIO
import time
from datetime import datetime 
import os

now = datetime.now()

relay = 37




def Run(sec):

	try:
		
		if (sec > 0):
			GPIO.setmode(GPIO.BOARD)
			GPIO.setup(relay,GPIO.OUT)
			print("Water pump open")
			print(datetime.now())
			GPIO.output(relay,GPIO.LOW)
			#os.system("sudo python /home/pi/Desktop/GardenAutomation/modules/segs.py")
			time.sleep(sec)
			#sec = sec - 1


		GPIO.output(relay,GPIO.HIGH)
		print("Water pump closed")
		print(datetime.now())
	
	except:
		print ("Water pump error")
		GPIO.output(relay,GPIO.HIGH)
		