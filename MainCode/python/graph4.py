import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pyplot
import datetime
import MySQLdb
import time, sys
import numpy

fig = pyplot.figure()

# Open database connection
db = MySQLdb.connect("localhost","danny","danny123","MYGARDEN" )
# prepare a cursor object using cursor() method
cursor = db.cursor()

x1 = []
y1 = []
y2 = []
y3 = []
y4 = []


x11 = []
y11 = []
y12 = []
y13 = []


font = {'family' : 'normal',
	'weight' : 'bold',
	'size'	: 8
	}

matplotlib.rc('font', **font)

x=0
y=0
xa=0
ya=0
yb=0
yc=0
cursor.execute("select max(cast(Data as decimal(16,2))),min(cast(Data as decimal(16,2))),avg(cast(Data as decimal(16,2))),cast(Datenow as date) Datenow from SenorLog where SensorName = 'temp sensor 2'  group by cast(Datenow as date)  order by cast(Datenow as date) ;" )
for row in cursor.fetchall():

	x = (row[3])
	y = (row[0])
	ya = (row[1])
	yb = (row[2])
	yc = (y-ya)
	x1.append(x)
	y1.append(y)
	y2.append(ya)
	y3.append(yb)
	y4.append(yc)
	
pyplot.title('Inside - MIN/MAX All time')
pyplot.xlabel('Time')
pyplot.ylabel('Temp C')

pyplot.grid(b='on')

pyplot.line = pyplot.plot(x1,y1, color='red',label='Max Temp')
pyplot.line = pyplot.plot(x1,y2, color='blue',label='Min Temp')
pyplot.line = pyplot.plot(x1,y3, color='green',label='Avg Temp')
pyplot.line = pyplot.plot(x1,y4, color='orange',label='Range Temp')

pyplot.legend(loc='best')

pyplot.savefig('/var/www/Graph4.png')
pyplot.clf()

