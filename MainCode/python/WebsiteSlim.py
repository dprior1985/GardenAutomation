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
vWaterExistsData = "555";
vRainData = "666";
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



cursor.execute("select SaveData from ControlLog where RunNumberId = (select max(RunNumberId) from RunNumber) and ActionName = 'WaterExists' ;" )
for row in cursor.fetchall():

	vWaterExistsData = (row[0])


cursor.execute("select SaveData from ControlLog where RunNumberId = (select max(RunNumberId) from RunNumber) and ActionName = 'Rain' ;" )
for row in cursor.fetchall():

	vRainData = (row[0])



t = datetime.datetime(2012, 2, 23, 0, 0)

#color = "Yellow"

#Avgtest = str(numpy.average(TempAvg))
#print("-----")
#print(Avgtest)
#print("-----")
#if (Avgtest == "nan"):
#	Avgtest = 0

#if (float(Avgtest) < 14):
#color = "Lightblue"
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
	vLastWaterLogicDesc ="NOT WATERED - <12 - toll cold"
if (vLastWaterLogic == "-3" ):
	vLastWaterLogicDesc ="NOT WATERED - Dont Water bewteen 9PM and 6AM"
if (vLastWaterLogic == "-6" ):
	vLastWaterLogicDesc ="NOT WATERED - Dont water within 6 hurs of last water"

if (vLastWaterLogic == "1" ):
	vLastWaterLogicDesc ="WATERED - error setting 1 not used"
if (vLastWaterLogic == "2" ):
	vLastWaterLogicDesc ="WATERED - water not exists water"
if (vLastWaterLogic == "3" ):
	vLastWaterLogicDesc ="WATERED - Not watered in 24 hours"
if (vLastWaterLogic == "4" ):
	vLastWaterLogicDesc ="WATERED - temp >= 12 < 16 then water"
if (vLastWaterLogic == "5" ):
	vLastWaterLogicDesc ="WATERED - temp >= 16  < 20 then water"
if (vLastWaterLogic == "6" ):
	vLastWaterLogicDesc ="WATERED - temp >= 20  then water"
if (vLastWaterLogic == "7" ):
	vLastWaterLogicDesc ="WATERED - error setting 7 not used"	
	
	
website="""
<!DOCTYPE html>
<html>
<head>

<link rel='stylesheet' type='text/css' href='/main.css'>
<link rel='stylesheet' type='text/css' href='main.css'>

</head>
<body bgcolour = "%s" >
<h2>Garden System:</h2>
<h3>Last time Watered (GMT):   %s</h3>
<img src='Graph1.png' alt='Graph1' style='width:500px;height:250px;'>
<img src='Graph2.png' alt='Graph2' style='width:500px;height:250px;'><br>
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
    <th>Watered</th>
    <td>%s</td>
    <th>Water Logic Used</th>
    <td>%s</td>
  </tr>
  <tr>
    <th>Water Present?</th>
    <td>%s</td>
    <th></th>
    <td></td>
  </tr>
  <tr>
    <th>Rain Sensor</th>
    <td>%s</td>
    <th></th>
    <td></td>
  </tr>
  <tr>
    <th>External - Temp Sensor 1</th>
    <td>%s</td>
    <th>Inside Bottle - Light Sensor 1</th>
    <td>%s</td>
  </tr>
  <tr>
    <th>With Pi - Temp Sensor 2</th>
    <td>%s</td>
    <th>Light Sensor 2</th>
    <td>%s</td>
  </tr>
  <tr>
    <th>Temp Sensor 3</th>
    <td>%s</td>
    <th></th>
    <td></td>
  </tr>
  <tr>
    <th>Temp Sensor 4</th>
    <td>%s</td>
    <th></th>
    <td></td>
  </tr>
  <tr>
    <th>Temp Sensor 5</th>
    <td>%s</td>
    <th></th>
    <td></td>
  </tr>
</table>
</body>
</html>
""" % (
 color
,vLastTimeWaterData
,vLastCheckDateData
,vLastCheckResultData
,vLastWaterLogicDesc
,vWaterExistsData
,vRainData 
,vTempsensor1
,vLightsensor1
,vTempsensor2
,vLightsensor2
,vTempsensor3
,vTempsensor4
,vTempsensor5

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
