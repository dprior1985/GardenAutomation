import datetime
from datetime import date
import MySQLdb
import time, sys
import numpy
import calendar

# Open database connection
db = MySQLdb.connect("localhost","danny","danny123","MYGARDEN" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
my_date = date.today()
vLastTimeWaterData = "000";
vLastWaterLogic = "";
vLastCheckDateData = "111";
vLastCheckResultData = "222";
vWeatherAPITempData = "333";
vWeatherAPIWeatherData = "444";
vWaterExistsData = "";
vRainData = "";
vURL = "/home/pi/Desktop/GardenAutomation/Pictures/Default.jpg";
vAPIUpdate = "";
vAPIwind = "";
vTempsensor1 = "";
vTempsensor2 = "";
vTempsensor3 = "";
vTempsensor4 = "";
vTempsensor5 = "";
TempAvg = []
ss = 0;
aa = 0;
vforecast1 = "";
vforecast2 = "";
vforecast3 = "";
vforecast4 = "";

LightAvg = []
vLightsensor1 = "";
vLightsensor2 = "";

Hall = ""
HallArray = []
H00 = ""
H01 = ""
H02 = ""
H03 = ""
H04 = ""
H05 = ""
H06 = ""
H07 = ""
H08 = ""
H09 = ""
H10 = ""
H11 = ""
H12 = ""
H13 = ""
H14 = ""
H15 = ""
H16 = ""
H17 = ""
H18 = ""
H19 = ""
H20 = ""
H21 = ""
H22 = ""
H23 = ""

cursor.execute("select concat_ws(' ',SaveData ,  cast(DateNow as char)) from ControlLog where ActionName = 'Weather API' and LogDescription = 'Weather' and datediff(now(),DateNow ) >= 0 and datediff(now(),DateNow ) <=24 and timestampdiff(HOUR,DateNow,NOW()) = 0  and minute(DateNow) <= 15 order by DateNow ; " )
for row in cursor.fetchall():
	H00 = (row[0])

cursor.execute("select concat_ws(' ',SaveData ,  cast(DateNow as char)) from ControlLog where ActionName = 'Weather API' and LogDescription = 'Weather' and datediff(now(),DateNow ) >= 0 and datediff(now(),DateNow ) <=24 and timestampdiff(HOUR,DateNow,NOW()) = 1  and minute(DateNow) <= 15 order by DateNow ; " )
for row in cursor.fetchall():
	H01 = (row[0])

cursor.execute("select concat_ws(' ',SaveData ,  cast(DateNow as char)) from ControlLog where ActionName = 'Weather API' and LogDescription = 'Weather' and datediff(now(),DateNow ) >= 0 and datediff(now(),DateNow ) <=24 and timestampdiff(HOUR,DateNow,NOW()) = 2  and minute(DateNow) <= 15 order by DateNow ; " )
for row in cursor.fetchall():
	H02 = (row[0])

cursor.execute("select concat_ws(' ',SaveData ,  cast(DateNow as char)) from ControlLog where ActionName = 'Weather API' and LogDescription = 'Weather' and datediff(now(),DateNow ) >= 0 and datediff(now(),DateNow ) <=24 and timestampdiff(HOUR,DateNow,NOW()) = 3  and minute(DateNow) <= 15 order by DateNow ; " )
for row in cursor.fetchall():
	H03 = (row[0])

cursor.execute("select concat_ws(' ',SaveData ,  cast(DateNow as char)) from ControlLog where ActionName = 'Weather API' and LogDescription = 'Weather' and datediff(now(),DateNow ) >= 0 and datediff(now(),DateNow ) <=24 and timestampdiff(HOUR,DateNow,NOW()) = 4  and minute(DateNow) <= 15 order by DateNow ; " )
for row in cursor.fetchall():
	H04 = (row[0])

cursor.execute("select concat_ws(' ',SaveData ,  cast(DateNow as char)) from ControlLog where ActionName = 'Weather API' and LogDescription = 'Weather' and datediff(now(),DateNow ) >= 0 and datediff(now(),DateNow ) <=24 and timestampdiff(HOUR,DateNow,NOW()) = 5  and minute(DateNow) <= 15 order by DateNow ; " )
for row in cursor.fetchall():
	H05 = (row[0])
	
cursor.execute("select concat_ws(' ',SaveData ,  cast(DateNow as char)) from ControlLog where ActionName = 'Weather API' and LogDescription = 'Weather' and datediff(now(),DateNow ) >= 0 and datediff(now(),DateNow ) <=24 and timestampdiff(HOUR,DateNow,NOW()) = 6  and minute(DateNow) <= 15 order by DateNow ; " )
for row in cursor.fetchall():
	H06 = (row[0])

cursor.execute("select concat_ws(' ',SaveData ,  cast(DateNow as char)) from ControlLog where ActionName = 'Weather API' and LogDescription = 'Weather' and datediff(now(),DateNow ) >= 0 and datediff(now(),DateNow ) <=24 and timestampdiff(HOUR,DateNow,NOW()) = 7  and minute(DateNow) <= 15 order by DateNow ; " )
for row in cursor.fetchall():
	H07 = (row[0])

cursor.execute("select concat_ws(' ',SaveData ,  cast(DateNow as char)) from ControlLog where ActionName = 'Weather API' and LogDescription = 'Weather' and datediff(now(),DateNow ) >= 0 and datediff(now(),DateNow ) <=24 and timestampdiff(HOUR,DateNow,NOW()) = 8  and minute(DateNow) <= 15 order by DateNow ; " )
for row in cursor.fetchall():
	H08 = (row[0])

cursor.execute("select concat_ws(' ',SaveData ,  cast(DateNow as char)) from ControlLog where ActionName = 'Weather API' and LogDescription = 'Weather' and datediff(now(),DateNow ) >= 0 and datediff(now(),DateNow ) <=24 and timestampdiff(HOUR,DateNow,NOW()) = 9  and minute(DateNow) <= 15 order by DateNow ; " )
for row in cursor.fetchall():
	H09 = (row[0])

cursor.execute("select concat_ws(' ',SaveData ,  cast(DateNow as char)) from ControlLog where ActionName = 'Weather API' and LogDescription = 'Weather' and datediff(now(),DateNow ) >= 0 and datediff(now(),DateNow ) <=24 and timestampdiff(HOUR,DateNow,NOW()) = 10  and minute(DateNow) <= 15 order by DateNow ; " )
for row in cursor.fetchall():
	H10 = (row[0])

cursor.execute("select concat_ws(' ',SaveData ,  cast(DateNow as char)) from ControlLog where ActionName = 'Weather API' and LogDescription = 'Weather' and datediff(now(),DateNow ) >= 0 and datediff(now(),DateNow ) <=24 and timestampdiff(HOUR,DateNow,NOW()) = 11  and minute(DateNow) <= 15 order by DateNow ; " )
for row in cursor.fetchall():
	H11 = (row[0])

cursor.execute("select concat_ws(' ',SaveData ,  cast(DateNow as char)) from ControlLog where ActionName = 'Weather API' and LogDescription = 'Weather' and datediff(now(),DateNow ) >= 0 and datediff(now(),DateNow ) <=24 and timestampdiff(HOUR,DateNow,NOW()) = 12  and minute(DateNow) <= 15 order by DateNow ; " )
for row in cursor.fetchall():
	H12 = (row[0])

cursor.execute("select concat_ws(' ',SaveData ,  cast(DateNow as char)) from ControlLog where ActionName = 'Weather API' and LogDescription = 'Weather' and datediff(now(),DateNow ) >= 0 and datediff(now(),DateNow ) <=24 and timestampdiff(HOUR,DateNow,NOW()) = 13  and minute(DateNow) <= 15 order by DateNow ; " )
for row in cursor.fetchall():
	H13 = (row[0])

cursor.execute("select concat_ws(' ',SaveData ,  cast(DateNow as char)) from ControlLog where ActionName = 'Weather API' and LogDescription = 'Weather' and datediff(now(),DateNow ) >= 0 and datediff(now(),DateNow ) <=24 and timestampdiff(HOUR,DateNow,NOW()) = 14  and minute(DateNow) <= 15 order by DateNow ; " )
for row in cursor.fetchall():
	H14 = (row[0])

cursor.execute("select concat_ws(' ',SaveData ,  cast(DateNow as char)) from ControlLog where ActionName = 'Weather API' and LogDescription = 'Weather' and datediff(now(),DateNow ) >= 0 and datediff(now(),DateNow ) <=24 and timestampdiff(HOUR,DateNow,NOW()) = 15  and minute(DateNow) <= 15 order by DateNow ; " )
for row in cursor.fetchall():
	H15 = (row[0])
	
cursor.execute("select concat_ws(' ',SaveData ,  cast(DateNow as char)) from ControlLog where ActionName = 'Weather API' and LogDescription = 'Weather' and datediff(now(),DateNow ) >= 0 and datediff(now(),DateNow ) <=24 and timestampdiff(HOUR,DateNow,NOW()) = 16  and minute(DateNow) <= 15 order by DateNow ; " )
for row in cursor.fetchall():
	H16 = (row[0])

cursor.execute("select concat_ws(' ',SaveData ,  cast(DateNow as char)) from ControlLog where ActionName = 'Weather API' and LogDescription = 'Weather' and datediff(now(),DateNow ) >= 0 and datediff(now(),DateNow ) <=24 and timestampdiff(HOUR,DateNow,NOW()) = 17  and minute(DateNow) <= 15 order by DateNow ; " )
for row in cursor.fetchall():
	H17 = (row[0])

cursor.execute("select concat_ws(' ',SaveData ,  cast(DateNow as char)) from ControlLog where ActionName = 'Weather API' and LogDescription = 'Weather' and datediff(now(),DateNow ) >= 0 and datediff(now(),DateNow ) <=24 and timestampdiff(HOUR,DateNow,NOW()) = 18  and minute(DateNow) <= 15 order by DateNow ; " )
for row in cursor.fetchall():
	H18 = (row[0])

cursor.execute("select concat_ws(' ',SaveData ,  cast(DateNow as char)) from ControlLog where ActionName = 'Weather API' and LogDescription = 'Weather' and datediff(now(),DateNow ) >= 0 and datediff(now(),DateNow ) <=24 and timestampdiff(HOUR,DateNow,NOW()) = 19  and minute(DateNow) <= 15 order by DateNow ; " )
for row in cursor.fetchall():
	H19 = (row[0])

cursor.execute("select concat_ws(' ',SaveData ,  cast(DateNow as char)) from ControlLog where ActionName = 'Weather API' and LogDescription = 'Weather' and datediff(now(),DateNow ) >= 0 and datediff(now(),DateNow ) <=24 and timestampdiff(HOUR,DateNow,NOW()) = 20  and minute(DateNow) <= 15 order by DateNow ; " )
for row in cursor.fetchall():
	H20 = (row[0])
	
cursor.execute("select concat_ws(' ',SaveData ,  cast(DateNow as char)) from ControlLog where ActionName = 'Weather API' and LogDescription = 'Weather' and datediff(now(),DateNow ) >= 0 and datediff(now(),DateNow ) <=24 and timestampdiff(HOUR,DateNow,NOW()) = 21  and minute(DateNow) <= 15 order by DateNow ; " )
for row in cursor.fetchall():
	H21 = (row[0])

cursor.execute("select concat_ws(' ',SaveData ,  cast(DateNow as char)) from ControlLog where ActionName = 'Weather API' and LogDescription = 'Weather' and datediff(now(),DateNow ) >= 0 and datediff(now(),DateNow ) <=24 and timestampdiff(HOUR,DateNow,NOW()) = 22  and minute(DateNow) <= 15 order by DateNow ; " )
for row in cursor.fetchall():
	H22 = (row[0])

cursor.execute("select concat_ws(' ',SaveData ,  cast(DateNow as char)) from ControlLog where ActionName = 'Weather API' and LogDescription = 'Weather' and datediff(now(),DateNow ) >= 0 and datediff(now(),DateNow ) <=24 and timestampdiff(HOUR,DateNow,NOW()) = 23  and minute(DateNow) <= 15 order by DateNow ; " )
for row in cursor.fetchall():
	H23 = (row[0])

	
cursor.execute("select cast(Water as char(50)) from RunNumber where RunNumberId = (select max(RunNumberId) from RunNumber) ;" )
for row in cursor.fetchall():

	vLastWaterLogic = (row[0])

cursor.execute("select SaveData from ControlLog where RunNumberId = (select max(RunNumberId) from RunNumber) and ActionName = 'light sensor 1' ;" )
for row in cursor.fetchall():

	vLightsensor1 = (row[0])
	LightAvg.append(float(vLightsensor1))
	
cursor.execute("select SaveData from ControlLog where RunNumberId = (select max(RunNumberId) from RunNumber) and ActionName = 'light sensor 2' ;" )
for row in cursor.fetchall():

	vLightsensor2 = (row[0])
	LightAvg.append(float(vLightsensor2))

cursor.execute("select SaveData from ControlLog where RunNumberId = (select max(RunNumberId) from RunNumber) and ActionName = 'temp sensor 1' ;" )
for row in cursor.fetchall():

	vTempsensor1 = (row[0])
	if ("not available" not in vTempsensor1):
		TempAvg.append(float(vTempsensor1))
		
	
cursor.execute("select SaveData from ControlLog where RunNumberId = (select max(RunNumberId) from RunNumber) and ActionName = 'temp sensor 2' ;" )
for row in cursor.fetchall():

	vTempsensor2 = (row[0])
	if ("not available" not in vTempsensor2):
		TempAvg.append(float(vTempsensor2))
		

cursor.execute("select SaveData from ControlLog where RunNumberId = (select max(RunNumberId) from RunNumber) and ActionName = 'temp sensor 3' ;" )
for row in cursor.fetchall():

	vTempsensor3 = (row[0])
	if ("not available" not in vTempsensor3):
		TempAvg.append(float(vTempsensor3))
		

cursor.execute("select SaveData from ControlLog where RunNumberId = (select max(RunNumberId) from RunNumber) and ActionName = 'temp sensor 4' ;" )
for row in cursor.fetchall():

	vTempsensor4 = (row[0])
	if ("not available" not in vTempsensor4):
		TempAvg.append(float(vTempsensor4))
		

cursor.execute("select SaveData from ControlLog where RunNumberId = (select max(RunNumberId) from RunNumber) and ActionName = 'temp sensor 5' ;" )
for row in cursor.fetchall():

	vTempsensor5 = (row[0])
	if ("not available" not in vTempsensor5):
		TempAvg.append(float(vTempsensor5))
		



cursor.execute("select max(DateNow) from RunNumber where water >0 ;" )
for row in cursor.fetchall():

	vLastTimeWaterData = (row[0])
	
	
cursor.execute("select DateNow from RunNumber where RunNumberId = (select max(RunNumberId) from RunNumber) ;" )
for row in cursor.fetchall():

	vLastCheckDateData = (row[0])


cursor.execute("select case when Water >= 1 then 'Watered' else 'Not Watered' end as aaa from RunNumber where RunNumberId = (select max(RunNumberId) from RunNumber) ;" )
for row in cursor.fetchall():

	vLastCheckResultData = (row[0])



cursor.execute("select SaveData from ControlLog where RunNumberId = (select max(RunNumberId) from RunNumber) and ActionName = 'Weather API' and LogDescription = 'Temp String' ;" )
for row in cursor.fetchall():

	vWeatherAPITempData = (row[0])


cursor.execute("select SaveData from ControlLog where RunNumberId = (select max(RunNumberId) from RunNumber) and ActionName = 'Weather API' and LogDescription = 'Weather' ;" )
for row in cursor.fetchall():

	vWeatherAPIWeatherData = (row[0])


cursor.execute("select SaveData from ControlLog where RunNumberId = (select max(RunNumberId) from RunNumber) and ActionName = 'WaterExists' ;" )
for row in cursor.fetchall():

	vWaterExistsData = (row[0])


cursor.execute("select SaveData from ControlLog where RunNumberId = (select max(RunNumberId) from RunNumber) and ActionName = 'Rain' ;" )
for row in cursor.fetchall():

	vRainData = (row[0])


cursor.execute("select SaveData from ControlLog where RunNumberId = (select max(RunNumberId) from RunNumber) and ActionName = 'Weather API' and LogDescription = 'Icon' ;" )
for row in cursor.fetchall():

	vURL = (row[0])


cursor.execute("select SaveData from ControlLog where RunNumberId = (select max(RunNumberId) from RunNumber) and ActionName = 'Weather API' and LogDescription = 'API Last Update' ;" )
for row in cursor.fetchall():

	vAPIUpdate = (row[0])

cursor.execute("select SaveData from ControlLog where RunNumberId = (select max(RunNumberId) from RunNumber) and ActionName = 'Weather API' and LogDescription = 'wind_string' ;" )
for row in cursor.fetchall():

	vAPIwind = (row[0])


cursor.execute("select SaveData from ControlLog where RunNumberId = (select max(RunNumberId) from RunNumber) and LogDescription = 'Forecast 1' ;" )
for row in cursor.fetchall():

	vforecast1 = (row[0])

cursor.execute("select SaveData from ControlLog where RunNumberId = (select max(RunNumberId) from RunNumber) and LogDescription = 'Forecast 2' ;" )
for row in cursor.fetchall():

	vforecast2 = (row[0])


cursor.execute("select SaveData from ControlLog where RunNumberId = (select max(RunNumberId) from RunNumber) and LogDescription = 'Forecast 3' ;" )
for row in cursor.fetchall():

	vforecast3 = (row[0])


cursor.execute("select SaveData from ControlLog where RunNumberId = (select max(RunNumberId) from RunNumber) and LogDescription = 'Forecast 4' ;" )
for row in cursor.fetchall():

	vforecast4 = (row[0])



t = datetime.datetime(2012, 2, 23, 0, 0)

#color = "Yellow"

#Avgtest = str(numpy.average(TempAvg))
#print("-----")
#print(Avgtest)
#print("-----")
#if (Avgtest == "nan"):
#	Avgtest = 0

#if (float(Avgtest) < 14):
#	color = "Lightblue"
#if (float(Avgtest) >= 14):

if (calendar.day_name[my_date.weekday()] == "Monday"):
	color = "PaleGoldenrod"
if (calendar.day_name[my_date.weekday()] == "Tuesday"):
	color = "Lavender"	
if (calendar.day_name[my_date.weekday()] == "Wednesday"):
	color = "PaleTurquoise"
if (calendar.day_name[my_date.weekday()] == "Thursday"):
	color = "Cornsilk"
if (calendar.day_name[my_date.weekday()] == "Friday"):
	color = "BlanchedAlmond"	
if (calendar.day_name[my_date.weekday()] == "Saturday"):
	color = "LightCoral"
if (calendar.day_name[my_date.weekday()] == "Sunday"):
	color = "PeachPuff"
	

	
vLastWaterLogicDesc =vLastWaterLogic

if (vLastWaterLogic == "0" ):
	vLastWaterLogicDesc ="NOT WATERED - ERROR NO CODE SELECTED"
if (vLastWaterLogic == "-1" ):
	vLastWaterLogicDesc ="NOT WATERED - <5 - too cold"
if (vLastWaterLogic == "-2" ):
        vLastWaterLogicDesc ="NOT WATERED - its raining"
if (vLastWaterLogic == "-3" ):
	vLastWaterLogicDesc ="NOT WATERED - error -3"
if (vLastWaterLogic == "-5" ):
	vLastWaterLogicDesc ="NOT WATERED - error -5"
if (vLastWaterLogic == "-6" ):
	vLastWaterLogicDesc ="NOT WATERED - error -6"
if (vLastWaterLogic == "-10" ):
        vLastWaterLogicDesc ="NOT WATERED - Not time to water -10"

if (vLastWaterLogic == "1" ):
	vLastWaterLogicDesc ="WATERED - Default setting"
if (vLastWaterLogic == "2" ):
	vLastWaterLogicDesc ="WATERED - ERROR 2"
if (vLastWaterLogic == "3" ):
	vLastWaterLogicDesc ="WATERED - temp >5 and < 12"
if (vLastWaterLogic == "4" ):
	vLastWaterLogicDesc ="WATERED - temp >= 12 < 16"
if (vLastWaterLogic == "5" ):
	vLastWaterLogicDesc ="WATERED - temp >= 16  < 20"
if (vLastWaterLogic == "6" ):
	vLastWaterLogicDesc ="WATERED - temp >= 20"
if (vLastWaterLogic == "7" ):
	vLastWaterLogicDesc ="WATERED - error 7"	
if (vLastWaterLogic == "8" ):
	vLastWaterLogicDesc ="WATERED - error 8"	
if (vLastWaterLogic == "9" ):
	vLastWaterLogicDesc ="WATERED - error 9"
if (vLastWaterLogic == "10" ):
	vLastWaterLogicDesc ="WATERED - Scheduled Water Time - But selection should have been made"
website="""
<!DOCTYPE html>
<html>
<head>

<link rel='stylesheet' type='text/css' href='/main.css'>
<link rel='stylesheet' type='text/css' href='main.css'>

</head>
<body bgcolour = "%s" >
<h2>Garden System:</h2>
<a href ="http://www.wunderground.com/personal-weather-station/dashboard?ID=IKENTBEX13">Click here for current weather</a><br>
<h3>Last time Watered (GMT):   %s</h3>
<img src='%s' alt='Logo' style='width:200px;height:228px;'><br>
<img src='Graph1.png' alt='Graph1' style='width:500px;height:250px;'>
<img src='Graph2.png' alt='Graph2' style='width:500px;height:250px;'><br>
<img src='Graph3.png' alt='Graph3' style='width:1000px;height:500px;'><br>
<img src='Graph4.png' alt='Graph4' style='width:1000px;height:500px;'><br>
<br>




<p> </p>
<table style='width:70%%'>
  <tr>
    <th>Garden System Last Checked Date (GMT)</th>
    <td>%s</td>
    <th></th>
    <td></td>
  </tr>
<p> </p> 
 <tr>
    <th>API Last Update (Local Time)</th>
    <td>%s</td>
    <th></th>
    <td></td>
  </tr>
  <tr>
    <th>Last Check Result</th>
    <td>%s</td>
    <th></th>
    <td></td>
  </tr>
  <tr>
    <th>API Current  Temp</th>
    <td>%s</td>
    <th>API Forecast</th>
    <td>%s</td>
  </tr>
  <tr>
    <th>API Current Weather</th>
    <td>%s</td>
    <th>API Forecast</th>
    <td>%s</td>
  </tr>
  <tr>
    <th>API Current  Wind</th>
    <td>%s</td>
    <th>API Forecast</th>
    <td>%s</td>
  </tr>
  <tr>
    <th></th>
    <td>%s</td>
    <th>API Forecast</th>
    <td>%s</td>
  </tr>
  <tr>
    <th></th>
    <td>%s</td>
    <th>Last Water Logic</th>
    <td>%s</td>
  </tr>
  <tr>
    <th>Internal - Temp Sensor</th>
    <td>%s</td>
    <th>Inside Bottle - Light Sensor 1</th>
    <td>%s</td>
  </tr>


  
   <tr>`
    <th>0 hours ago </th>
    <td>%s</td>
    <th>1 hour ago</th>
    <td>%s</td>
  </tr>
  
  <tr>
    <th>2 hours ago </th>
    <td>%s</td>
    <th>3 hours ago</th>
    <td>%s</td>
  </tr>

  <tr>
    <th>4 hours ago </th>
    <td>%s</td>
    <th>5 hours ago</th>
    <td>%s</td>
  </tr>

  <tr>
    <th>6 hours ago </th>
    <td>%s</td>
    <th>7 hours ago</th>
    <td>%s</td>
  </tr>

  <tr>
    <th>8 hours ago </th>
    <td>%s</td>
    <th>9 hours ago</th>
    <td>%s</td>
  </tr>

  <tr>
    <th>10 hours ago </th>
    <td>%s</td>
    <th>11 hours ago</th>
    <td>%s</td>
  </tr>

  <tr>
    <th>12 hours ago </th>
    <td>%s</td>
    <th>13 hours ago</th>
    <td>%s</td>
  </tr>

  <tr>
    <th>14 hours ago </th>
    <td>%s</td>
    <th>15 hours ago</th>
    <td>%s</td>
  </tr>

  <tr>
    <th>16 hours ago </th>
    <td>%s</td>
    <th>17 hours ago</th>
    <td>%s</td>
  </tr>


  <tr>
    <th>18 hours ago </th>
    <td>%s</td>
    <th>19 hours ago</th>
    <td>%s</td>
  </tr>


  <tr>
    <th>20 hours ago </th>
    <td>%s</td>
    <th>21 hours ago</th>
    <td>%s</td>
  </tr>  

  <tr>
    <th>22 hours ago </th>
    <td>%s</td>
    <th>23 hours ago</th>
    <td>%s</td>
  </tr>  
  
</table>
</body>
</html>
""" % (
 color
,vLastTimeWaterData
,vURL
,vLastCheckDateData
,vAPIUpdate
,vLastCheckResultData
,vWeatherAPITempData 
,vforecast1
,vWeatherAPIWeatherData
,vforecast2
,vAPIwind
,vforecast3
,vWaterExistsData
,vforecast4 
,vRainData 
,vLastWaterLogicDesc
,vTempsensor2
,vLightsensor1
,H00
,H01
,H02
,H03
,H04
,H05
,H06
,H07
,H08
,H09
,H10
,H11
,H12
,H13
,H14
,H15
,H16
,H17
,H18
,H19
,H20
,H21
,H22
,H23
)


#Removed from parameters
#,numpy.average(TempAvg)
#,numpy.average(LightAvg)

#Removed from HTML
#  <tr>
#    <th>Average Temp Sensor</th>
#     <td>%s</td>
#    <th>Average Light</th>
#    <td>%s</td>
#  </tr>


css="""body {
    background-color: %s;
}

h2 {
    color: navy;
    margin-left: 20px;
}

h3 {
    color: Black;
    margin-left: 30px;
}

table, th, td {
    border: 3px solid black;
    border-collapse: collapse;
	
}
th, td {
    padding: 5px;
    text-align: left;
	color:Green
}
""" % (
color
)

#print website;
fo = open("/var/www/index.html", "w")

fo.seek(0, 2)
line = fo.write( website )

# Close opend file
fo.close()


#print css;
io = open("/var/www/main.css", "w")

io.seek(0, 2)
line = io.write( css )

# Close opend file
io.close()


print('SITE CREATED')
print(datetime.datetime.now())

