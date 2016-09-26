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

cursor.execute("select max(cast(SaveData as decimal(16,2))),min(cast(SaveData as decimal(16,2))),cast(Datenow as date) Datenow from ControlLog where ActionName = 'Weather API' and LogDescription = 'Temp C' group by cast(Datenow as date)   order by cast(Datenow as date) ;" )
for row in cursor.fetchall():

	x = (row[2])
	y = (row[0])
	ya = (row[1])
	x1.append(x)
	y1.append(y)
	y2.append(ya)

pyplot.title('API - MIN/MAX All time')
pyplot.xlabel('Time')
pyplot.ylabel('Temp C')

pyplot.grid(b='on')

pyplot.line = pyplot.plot(x1,y1, color='red',label='Max Temp')
pyplot.line = pyplot.plot(x1,y2, color='blue',label='Min Temp')

pyplot.legend(loc='best')

pyplot.savefig('/var/www/Graph3.png')
pyplot.clf()
