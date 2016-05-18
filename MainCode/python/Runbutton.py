import RPi.GPIO as GPIO
from datetime import datetime 
import time
import os
import sys

sys.path.append('/home/pi/Desktop/GardenAutomation/modules')

import openrelay

GPIO.setmode(GPIO.BOARD)
GPIO.setup(35,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)

start = datetime.now()
now = datetime.now()
count = 0
check = 1
while check == 1:
	inputValue = GPIO.input(35)
	now = datetime.now()
	if (inputValue ==True):
		try:
			if (now.minute < 59):
				count = count + 1
				print("Button pressed running openrelay.py" )
				print(now)
				openrelay.Run(10)
				
		except:
			print("Error running Main.sh")
			count = count + 1 
	if (now.minute >= 59):
		check = 0
	
	time.sleep(.1)


