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

cursor.execute("select cast(SaveData as decimal(16,2)),Datenow from ControlLog where ActionName = 'Weather API' and LogDescription = 'Temp C'  and subtime(now(), '96:00:00') <= DateNow order by DateNow;" )
for row in cursor.fetchall():

	x = (row[1])
	y = (row[0])
	x1.append(x)
	y1.append(y)

#cursor.execute("select Data,Datenow from SenorLog where SensorName = 'temp sensor 2' order by DateNow;" )

#for row in cursor.fetchall():

#	y = (row[0])
#	y2.append(y)





#pyplot.title('Temp Senors for last 24 hours')
pyplot.title('API - Last 2 days')
pyplot.xlabel('Time')
pyplot.ylabel('Temp C')

pyplot.grid(b='on')


pyplot.line = pyplot.plot(x1,y1, color='green',label='API Weather Station')
#pyplot.line = pyplot.plot(x1,y2, color='red',label='Temp Senor 2')

pyplot.legend(loc='best')

pyplot.savefig('/var/www/Graph1.png')
pyplot.clf()




#cursor.execute("select cast(Data as decimal(16,2)),Datenow from SenorLog where SensorName = 'temp sensor 2' and subtime(now(), '24:00:00') <= DateNow order by DateNow; " )
#for row in cursor.fetchall():

#	xa = (row[1])
#	ya = (row[0])
#	x11.append(xa)
#	y11.append(ya)

#cursor.execute("select Data,Datenow from SenorLog where SensorName = 'temp sensor 2' and subtime(now(), '24:00:00') <= DateNow order by DateNow; " )

#for row in cursor.fetchall():

#	ya = (row[0])
#	y12.append(ya)


#pyplot.title('Temp Senors for last 24 hours')
#pyplot.legend(loc='best')
#pyplot.grid(b='on')

#pyplot.line = pyplot.plot(x11,y11, color='green',label='Temp Senor 1')
#pyplot.line = pyplot.plot(x11,y12, color='red',label='Inside Temp - Last 24 Hours')

#pyplot.savefig('/var/www/Graph2.png')
