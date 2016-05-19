
import MySQLdb



# Open database connection
db = MySQLdb.connect("localhost","danny","danny123","MYGARDEN" )
# prepare a cursor object using cursor() method
cursor = db.cursor()



cursor.execute("delete from ControlLog 	where DateNow 	< cast('01-June-2016' as date) ;" )
cursor.execute("delete from RunNumber 	where DateNow 	< cast('01-June-2016' as date) ;" )
cursor.execute("delete from SenorLog	where DateNow 	< cast('01-June-2016' as date) ;" )

