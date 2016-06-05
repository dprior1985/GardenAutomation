#Version 1.0
# 31/08/2015 - danny prior
# this script will allow for a automated garden water system which uses senors to determine what needs to be watered


import urllib2
import json
import RPi.GPIO as GPIO
import time
import MySQLdb
import datetime
import time
import os
import sys

sys.path.append('/home/pi/Desktop/GardenAutomation/modules')
import lightsensor
import openrelay
import TemperatureSenor
		
		
# Open database connection
db = MySQLdb.connect("localhost","danny","danny123","MYGARDEN" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
Weather1 ="";
RunNumber = 0;
Water = 0;
cnt = 0;
icon_url = "";

#GPIO PINS SETUP
GPIO.setmode(GPIO.BOARD)

watertest = 40; # GPIO pin number
GPIO.setup(watertest,GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #PUD_DOWN pulls down GPIO from third state (random) to 2 state pin (true or false). found this out as results where coming back random


Rain = 11; # GPIO pin number
GPIO.setup(Rain,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)




insert ="INSERT INTO ControlLog(LogDescription,ActionName,SaveData,ControlId,DateNow)";
sql3 = "";		

def main():

		
	global Water;

	try:
	   # Execute the SQL command
   		cursor.execute("update ControlLog set Active =0 where Active = 1")
	   # Commit your changes in the database
		db.commit()
	except:
	   	db.rollback()
		
	print "Runnumber classmethod"
	print(datetime.datetime.now())
	RunNumber()
	print "watar classmethod"
	print(datetime.datetime.now())
	water()
	print "Rain classmethod"
	print(datetime.datetime.now())	
	rain()
	print "light classmethod"
	print(datetime.datetime.now())
	light()
	print "Temperature classmethod"
	print(datetime.datetime.now())
	temperature()
	try:
	   # Execute the SQL command
	   	print "SQL3 exec"
		print(datetime.datetime.now())
   		cursor.execute(sql3)
	   # Commit your changes in the database
		db.commit()
	except:
	   	db.rollback()
	print "decide classmethod"
	print(datetime.datetime.now())

	decide()
	
	if (Water >= 2):
		print "openrelay classmethod"
		print(datetime.datetime.now())
		if (Water == 1):	
			openrelay.Run(30)
		
		if (Water == 2):	
			openrelay.Run(20)
		
		if (Water == 3):	
			openrelay.Run(60)
		
		if (Water == 4):	
			openrelay.Run(30)
		
		if (Water == 5):	
			openrelay.Run(30)
			time.sleep(10)
			openrelay.Run(10)
		
		if (Water == 6):	
			openrelay.Run(20)
		
		if (Water == 7):	
			openrelay.Run(20)
		
		if (Water == 8):	
			openrelay.Run(40)
			time.sleep(10)
			openrelay.Run(10)		
		
		if (Water == 9):	
			openrelay.Run(60)
			time.sleep(10)
			openrelay.Run(10)
			
		if (Water == 10):	
			openrelay.Run(60)

	if (Water == 0):
		print('Not Active')
		print(datetime.datetime.now())


	print "END"
	print(datetime.datetime.now())


# disconnect from server
	db.close()

def light():
	print("33 start")
	light1 = lightsensor.RCtime(33)
	print("33 end")
#	light2 = lightsensor.RCtime(36)
	sql1 =  insert +" values('light sensor','light sensor 1','%s',1,now() );" % light1   
#	sql2 =  insert +" values('light sensor','light sensor 2','%s',1,now() );" % light2  
	
	# Execute the SQL command
  	cursor.execute(sql1)
#	cursor.execute(sql2)
	
def temperature():
	

	temperature1 =	TemperatureSenor.Sensor("28-0115524404ff")
	temperature2 =	TemperatureSenor.Sensor("28-031553a54dff")
	temperature3 =	TemperatureSenor.Sensor("28-031553aaf4ff")
	temperature4 =	TemperatureSenor.Sensor("28-031553aca3ff")
	temperature5 =	TemperatureSenor.Sensor("28-031553b046ff")

	sql1 =  insert +" values('temp sensor','temp sensor 1','%s',1,now() );" % temperature1   
	sql2 =  insert +" values('temp sensor','temp sensor 2','%s',1,now() );" % temperature2  
	sql3 =  insert +" values('temp sensor','temp sensor 3','%s',1,now() );" % temperature3
	sql4 =  insert +" values('temp sensor','temp sensor 4','%s',1,now() );" % temperature4 
	sql5 =  insert +" values('temp sensor','temp sensor 5','%s',1,now() );" % temperature5  

 
	# Execute the SQL command
  	cursor.execute(sql1)
	cursor.execute(sql2)
	cursor.execute(sql3)
	cursor.execute(sql4)
	cursor.execute(sql5)



	
def decide():

	global Water;

	waterlogic = 1;
#Default to water
	sq53 =  "update RunNumber set Water = 1 where  RunnumberId in (select RunNumberId from ControlLog and RunNumberId = %s ;" %  (int(RunNumber))
	
	try:
	   # Execute the SQL command
   		cursor.execute(sq53)
	   # Commit your changes in the database
		db.commit()
		waterlogic = 1;
	except:
		print "failure default to water"
	   	db.rollback()

#if temp < 12 then dont water
	sq53 =  "update RunNumber set Water = -1 where Water >= 0 and  RunnumberId in (select RunNumberId from ControlLog where SavedDataInt < 12 and Active = 1 ) and RunNumberId = %s ;" %  (int(RunNumber))
	
	try:
	   # Execute the SQL command
   		cursor.execute(sq53)
	   # Commit your changes in the database
		db.commit()
		waterlogic = -1;
	except:
		print "failure with temp <12 "
	   	db.rollback()

#if water not exists water
	sq53 =  "update RunNumber set Water = 2 where Water <= 0 and  RunnumberId in (select RunNumberId from ControlLog where ActionName = 'WaterExists' and Active = 1 and SaveData = 'No' ) and RunNumberId = %s ;" %  (int(RunNumber))
	try:
	   # Execute the SQL command
   		cursor.execute(sq53)
	   # Commit your changes in the database
		db.commit()
		waterlogic = 2;
	except:
		print "failure with water not exists"
	   	db.rollback()
		
		
#if temp >= 12 < 16 then water
	sq53 =  "update RunNumber set Water = 4 where Water <= 0 and  RunnumberId in (select RunNumberId from ControlLog where SavedDataInt >=12 and SavedDataInt < 16 and Active = 1 ) and RunNumberId = %s ;" %  (int(RunNumber))
	
	try:
	   # Execute the SQL command
   		cursor.execute(sq53)
	   # Commit your changes in the database
		db.commit()
		waterlogic = 4;
	except:
		print "failure with temp >=12 < 16 then water "
	   	db.rollback()

#if temp >= 16  < 20 then water
	sq53 =  "update RunNumber set Water = 5 where Water <= 0 and  RunnumberId in (select RunNumberId from ControlLog where SavedDataInt >=16 and SavedDataInt < 20 and Active = 1 ) and RunNumberId = %s ;" %  (int(RunNumber))
	
	try:
	   # Execute the SQL command
   		cursor.execute(sq53)
	   # Commit your changes in the database
		db.commit()
		waterlogic = 5;
	except:
		print "failure with temp >16  < 20 then water "
	   	db.rollback()
		
#if temp >= 20  then water
	sq53 =  "update RunNumber set Water = 6 where Water <= 0 and  RunnumberId in (select RunNumberId from ControlLog where SavedDataInt >=20 and Active = 1 ) and RunNumberId = %s ;" %  (int(RunNumber))
	
	try:
	   # Execute the SQL command
   		cursor.execute(sq53)
	   # Commit your changes in the database
		db.commit()
		waterlogic = 6;
	except:
		print "failure with temp >= 20  then water "
	   	db.rollback()

		
		

# #if local senor says raining then dont water	
	# sq531 =  "update RunNumber set Water = -2 where Water > 0 and  RunnumberId in (select RunNumberId from ControlLog where (ActionName like '%%Rain%%' or ActionName like '%%rain%%' ) and Active = 1 and SaveData = 'Yes' ) and RunNumberId = %s ;" %  (int(RunNumber))
	
	# try:
	   # # Execute the SQL command
   		# cursor.execute(sq531)
	   # # Commit your changes in the database
		# db.commit()
	# except:
		# print "failure with local rain senor"
	   	# db.rollback()










		
# #if rained in last 6 hours dont water
	# sq53 =  "update RunNumber set Water = -4 where Water > 0 and RunnumberId in ( select distinct %s  from (select distinct RunnumberId from ControlLog where (ActionName like '%%Rain%%' or ActionName like '%%rain%%') and SaveData = 'Yes' and datediff(now(),DateNow ) = 0 and timestampdiff(HOUR,DateNow,NOW()) <= 6 union select distinct RunnumberId from ControlLog where ActionName = 'Weather API' and SaveData Like 'Rain' and datediff(now(),DateNow ) = 0 and timestampdiff(HOUR,DateNow,NOW()) <= 6  ) as e)  ;" %  (int(RunNumber))
	# try:
	   # # Execute the SQL command
   		# cursor.execute(sq53)
	   # # Commit your changes in the database
		# db.commit()
	# except:
		# print "-------------"
		# print sq53
		# print "failure if rained in last 6 hours dont water"
	   	# db.rollback()



#if water exists water

	sq53 =  "update RunNumber set Water = -5 where Water >= 0 and  RunnumberId in (select RunNumberId from ControlLog where ActionName = 'WaterExists' and Active = 1 and SaveData = 'Yes' ) and RunNumberId = %s ;" %  (int(RunNumber))
	try:
	   # Execute the SQL command
   		cursor.execute(sq53)
	   # Commit your changes in the database
		db.commit()
		waterlogic = -5;
	except:	
		print "failure with water exists"
	   	db.rollback()
		
		
#Test Relay - Disable after test
	# sq53 =  "update RunNumber set Water = 10 where RunNumberId = %s ;" %  (int(RunNumber))
	# try:
	   # # Execute the SQL command
   		# cursor.execute(sq53)
	   # # Commit your changes in the database
		# db.commit()
	# except:	
		# print "failure with test"
	   	# db.rollback()

	
#if before 6am or after 9PM dont watar
	if (waterlogic <> 2):
		sq53 =  "update RunNumber set Water = -3 where  Water >= 0 and (hour(now()) >= 21 or hour(now()) <= 5 ) and RunNumberId = %s ;" %  (int(RunNumber))
		try:
		   # Execute the SQL command
			cursor.execute(sq53)
		   # Commit your changes in the database
			db.commit()
			waterlogic = -3;
		except:
			print "failure with before 6am or 9pm"
			db.rollback()	
	

#if watered in last 3 hours dont water
	sq53 =  "update RunNumber set Water = -6 where Water >= 0 and  RunnumberId in ( select %s from (select * from RunNumber where Water >= 1 and cast(timestampdiff(hour,now(),DateNow ) as signed) <= 0 and cast(timestampdiff(HOUR,NOW(),DateNow) as signed) >= -3 and date(now()) = date(DateNow))  e);" %  (int(RunNumber))
	try:
	   # Execute the SQL command
   		cursor.execute(sq53)
	   # Commit your changes in the database
		db.commit()
		waterlogic = -6;
	except:
		print "-------------"
		print sq53
		print "if not watered in 3 hours water"
	   	db.rollback()
		
# #if not watered in 23 hours water
	# sq53 =  "update RunNumber set Water = 3 where Water <= 0 and RunnumberId = %s and 23 >= ( select count(*) from (select distinct RunnumberId from RunNumber where Water <= 0 and timestampdiff(hour,now(),DateNow ) >= 0 and timestampdiff(HOUR,DateNow,NOW()) <= 24 ) e);" %  (int(RunNumber))
	# try:
	   # # Execute the SQL command
   		# cursor.execute(sq53)
	   # # Commit your changes in the database
		# db.commit()
	# except:
		# print "-------------"
		# print sq53
		# print "if not watered in 24 hours water"
	   	# db.rollback()
		


		
#if temp >= 12 < 16 then water and not in 23 hours
	sq53 =  "update RunNumber set Water = 7 where Water <= 0 and  RunnumberId in (select RunNumberId from ControlLog where SavedDataInt >=12 and SavedDataInt < 16 and Active = 1 ) and 23 >= ( select count(*) from (select distinct RunnumberId from RunNumber where Water <= 0 and timestampdiff(hour,now(),DateNow ) >= 0 and timestampdiff(HOUR,DateNow,NOW()) <= 24 ) and RunNumberId = %s ;" %  (int(RunNumber))
	
	try:
	   # Execute the SQL command
   		cursor.execute(sq53)
	   # Commit your changes in the database
		db.commit()
		waterlogic = 7;
	except:
		print "failure with temp >=12 < 16 then water "
	   	db.rollback()

#if temp >= 16  < 20 then water and not in 23 hours
	sq53 =  "update RunNumber set Water = 8 where Water <= 0 and  RunnumberId in (select RunNumberId from ControlLog where SavedDataInt >=16 and SavedDataInt < 20 and Active = 1 ) and 23 >= ( select count(*) from (select distinct RunnumberId from RunNumber where Water <= 0 and timestampdiff(hour,now(),DateNow ) >= 0 and timestampdiff(HOUR,DateNow,NOW()) <= 24 ) and RunNumberId = %s ;" %  (int(RunNumber))
	
	try:
	   # Execute the SQL command
   		cursor.execute(sq53)
	   # Commit your changes in the database
		db.commit()
		waterlogic = 8;
	except:
		print "failure with temp >16  < 20 then water "
	   	db.rollback()
		
#if temp >= 20  then water and not in 23 hours
	sq53 =  "update RunNumber set Water = 9 where Water <= 0 and  RunnumberId in (select RunNumberId from ControlLog where SavedDataInt >=20 and Active = 1 ) and 23 >= ( select count(*) from (select distinct RunnumberId from RunNumber where Water <= 0 and timestampdiff(hour,now(),DateNow ) >= 0 and timestampdiff(HOUR,DateNow,NOW()) <= 24 ) and RunNumberId = %s ;" %  (int(RunNumber))
	
	try:
	   # Execute the SQL command
   		cursor.execute(sq53)
	   # Commit your changes in the database
		db.commit()
		waterlogic = 9;
	except:
		print "failure with temp >= 20  then water "
	   	db.rollback()

# if not watered in 23 hours water
	# # sq53 =  "update RunNumber set Water = 3 where Water <= 0 and RunnumberId = %s and 23 >= ( select count(*) from (select distinct RunnumberId from RunNumber where Water <= 0 and timestampdiff(hour,now(),DateNow ) >= 0 and timestampdiff(HOUR,DateNow,NOW()) <= 24 ) e);" %  (int(RunNumber))
	# # try:
	   # Execute the SQL command
   		# # cursor.execute(sq53)
	   # Commit your changes in the database
		# # db.commit()
	# # except:
		# # print "-------------"
		# # print sq53
		# # print "if not watered in 23 hours water"
	   	# # db.rollback()		

		
#if schedule run
	sq53 =  "update RunNumber set Water = 10 where RunnumberId = %s and hour(now()) in ( select Time from Schedule ) e);" %  (int(RunNumber))
	try:
	   # Execute the SQL command
   		cursor.execute(sq53)
	   # Commit your changes in the database
		db.commit()
	except:
		print "-------------"
		print sq53
		print "error schedule run"
	   	db.rollback()		
		

		


	cursor.execute("select Water from RunNumber where RunNumberId = %s ;" %  (int(RunNumber)))
	for row in cursor.fetchall():

		Water = (row[0])



def RunNumber():

	sql =  "insert into RunNumber(DateNow,Water)  values(now(),0);"
	
	try:
	   # Execute the SQL command
   		cursor.execute(sql)
	   # Commit your changes in the database
		db.commit()

	except:
	#   # Rollback in case there is any error
	   	print "failure with run number"
		db.rollback()
		
	
	global RunNumber;
	global sql3;

	cursor.execute("select RunNumberID from RunNumber ORDER BY RunNumberId DESC limit 1")
	for row in cursor.fetchall():

		RunNumber = (row[0])
	
	sql3 =  "update ControlLog set RunNumberId = %s ,Active = 1 where RunNumberId is null ;" %  (int(RunNumber))
			
	

	
def water():

	inputValue = GPIO.input(watertest)
	if (inputValue ==True):

		sql1 = insert +" values('Water','WaterExists','Yes',2,now() );" 
				
	else:			
		sql1 = insert +" values('No Water','WaterExists','No',2,now() );" 
	
	try:
	   # Execute the SQL command
   		cursor.execute(sql1)
   	   # Commit your changes in the database
		db.commit()
	except:
		print "failure with water check"
	   	db.rollback()


def rain():

	inputValue = GPIO.input(Rain)
	if (inputValue ==True):
		sql1 = insert +" values('Raining','Rain','Yes',5,now() );" 
				
	else:
			
		sql1 = insert +" values('Not Raining','Rain','No',5,now() );" 
	
	try:
	   # Execute the SQL command
   		cursor.execute(sql1)
   	   # Commit your changes in the database
		db.commit()
	except:
		print "failure with rain check"
	   	db.rollback()
	


if __name__ == '__main__':
	main()

 	GPIO.cleanup()
