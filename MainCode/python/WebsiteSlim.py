import datetime
import MySQLdb
import time, sys
import numpy

# Open database connection
db = MySQLdb.connect("localhost","danny","danny123","MYGARDEN" )
# prepare a cursor object using cursor() method
cursor = db.cursor()

vLastTimeWaterData = "000";

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
color = "PeachPuff"
	
 
website="""
<!DOCTYPE html>
<html>
<head>

<link rel='stylesheet' type='text/css' href='/main.css'>
<link rel='stylesheet' type='text/css' href='main.css'>

</head>
<body bgcolour = "%s" >
<h2>Garden System:</h2>
<a href ="http://www.wunderground.com/personal-weather-station/dashboard?ID=IKENTBEX3">Click here for current weather</a><br>
<h3>Last time Watered (GMT):   %s</h3>
<img src='Graph1.png' alt='Graph1' style='width:1000px;height:500px;'><br>
<img src='Graph2.png' alt='Graph2' style='width:1000px;height:500px;'><br>
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
    <th></th>
    <td></td>
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
    <th>Inside Bottle - Temp Sensor 2</th>
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
