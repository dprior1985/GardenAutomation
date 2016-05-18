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


cursor.execute("select SaveData,Datenow from ControlLog where ActionName = 'light sensor 1' order by DateNow; ;" )
for row in cursor.fetchall():

	x = (row[1])
	y = (row[0])
	x1.append(x)
	y1.append(y)

pyplot.title('Light Senors for all time')
pyplot.xlabel('Time')
pyplot.ylabel('mil secs')

pyplot.grid(b='on')


pyplot.line = pyplot.plot(x1,y1, color='green',label='Light Senor')

pyplot.legend(loc='best')

pyplot.savefig('/var/www/LightGraph1.png')
pyplot.clf()
