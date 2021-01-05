import mysql.connector

db = mysql.connector.connect(
	host = "localhost",
	user= "root",
	#user="datarep" #mac username
    #passwd="password" #mac password
	password = "root",
	)
	
cursor = db.cursor()
sql = "CREATE database datarepresentation"
cursor.execute(sql)