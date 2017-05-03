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


x11 = []
y11 = []
y12 = []

font = {'family' : 'normal',
	'weight' : 'bold',
	'size'	: 8
	}

matplotlib.rc('font', **font)

x=0
y=0
xa=0
ya=0

cursor.execute("select cast(Data as decimal(16,2)),Datenow from SenorLog where SensorName = 'temp sensor 2' and subtime(now(), '96:00:00') <= DateNow order by DateNow; " )
for row in cursor.fetchall():

	xa = (row[1])
	ya = (row[0])
	x11.append(xa)
	y11.append(ya)

#cursor.execute("select Data,Datenow from SenorLog where SensorName = 'temp sensor 2' and subtime(now(), '48:00:00') <= DateNow order by DateNow; " )

#for row in cursor.fetchall():

#	ya = (row[0])
#	y12.append(ya)


pyplot.title('Temp Senors for last 48 hours')

pyplot.xlabel('Time')
pyplot.ylabel('Temp C')

pyplot.grid(b='on')

pyplot.legend(loc='best')

pyplot.line = pyplot.plot(x11,y11, color='red',label='Inside Temp - Last 4 days')


pyplot.savefig('/var/www/Graph2.png')
