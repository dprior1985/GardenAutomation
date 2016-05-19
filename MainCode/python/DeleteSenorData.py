
import MySQLdb



# Open database connection
db = MySQLdb.connect("localhost","danny","danny123","MYGARDEN" )
# prepare a cursor object using cursor() method
cursor = db.cursor()



cursor.execute("delete from ControlLog 	where DateNow 	< date_format(str_to_date('02/06/2016' ,'%d/%m/%Y'),'%Y%m%d') ;" )
cursor.execute("delete from RunNumber 	where DateNow 	< date_format(str_to_date('02/06/2016' ,'%d/%m/%Y'),'%Y%m%d') ;" )
cursor.execute("delete from SenorLog	where DateNow 	< date_format(str_to_date('02/06/2016' ,'%d/%m/%Y'),'%Y%m%d') ;" )

