import RPi.GPIO as GPIO
from datetime import datetime 
import time

import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(38,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)

now = datetime.now()
count = 0
check = 1
print("Test Run")
print(now)
while check == 1:
	inputValue = GPIO.input(38)
	now = datetime.now()
	if (inputValue ==True):
		try:
			if (now.minute < 59):
				count = count + 1
#				print("running LCD")
#				os.system("sudo python /home/pi/Desktop/GardenAutomation/MainCode/python/lcd_weather.py")
				print("Button pressed running Main.sh" )
				print(now)
				os.system("sudo /home/pi/Desktop/GardenAutomation/MainCode/scripts/Main.sh")

					
		except:
			print("Error running Main.sh")
			count = count + 1
	if (now.minute >=59):
		check = 0
	
	time.sleep(.1)


