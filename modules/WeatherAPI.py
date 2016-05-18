import RPi.GPIO as GPIO
import datetime
import os
import time
import urllib2
import json

def API(API):

	try:
		if (API == "geolookup"):
			#bexleyheath personal weather station				
			f = urllib2.urlopen('http://api.wunderground.com/api/2bdf859af15fee8d/geolookup/conditions/q/PWS:IKENTBEX3.json')
		if (API =="forecast"):
			#bexleyheath personal weather station				
			f = urllib2.urlopen('http://api.wunderground.com/api/2bdf859af15fee8d/forecast/conditions/q/PWS:IKENTBEX3.json')

	#get API weather data from underground weather
		json_string = f.read()
		
	
	except:
		print("API module failure")
		
		
	return  str(json_string);