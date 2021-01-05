import mysql.connector

db = mysql.connector.connect(
	host = "localhost",
	user= "root",
	password = "root",
    #user="datarep" #mac username
    #passwd="password" #mac password
    database= "datarepresentation"
	)
	
cursor = db.cursor()
sql = "CREATE table capitals(id int PRIMARY KEY, name varchar(250), country varchar(250), population int)"
cursor.execute(sql)