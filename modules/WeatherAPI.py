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
			#f = urllib2.urlopen('http://api.wunderground.com/api/90b24aac53db4186/geolookup/conditions/q/PWS:IKENTBEX4.json')
			f = urllib2.urlopen('http://api.wunderground.com/api/90b24aac53db4186/geolookup/conditions/q/PWS:IKENTBEX13.json')			
		if (API =="forecast"):
			#bexleyheath personal weather station				
			#f = urllib2.urlopen('http://api.wunderground.com/api/90b24aac53db4186/forecast/conditions/q/PWS:IKENTBEX4.json')
			f = urllib2.urlopen('http://api.wunderground.com/api/90b24aac53db4186/forecast/conditions/q/PWS:IKENTBEX13.json')

	#get API weather data from underground weather
		json_string = f.read()
		
	
	except:
		print("API module failure")
		
		
	return  str(json_string);
