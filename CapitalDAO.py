import mysql.connector
import dbconfig as cfg

class CapitalDAO:
    db =""
    # These are read in from a configuration file.
    def __init__(self):
        self.db = mysql.connector.connect(
            host = cfg.mysql["host"],
            user = cfg.mysql["user"],
            password = cfg.mysql["password"],
            #user="datarep" #mac username
            #passwd="password" #mac password
            database = cfg.mysql["database"]
            )

    def create(self, capital):
        cursor = self.db.cursor()
        sql = "insert into capitals (id, name, country, population) values (%s, %s, %s, %s)"
        values = [
            capital['id'],
            capital['name'],
            capital['country'],
            capital['population']
        ]
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = "select * from capitals"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
        return returnArray

    def findById(self, id):
        cursor = self.db.cursor()
        sql = "select * from capitals where id = %s"
        values = [id]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        resultAsDict = self.convertToDict(result)
        return resultAsDict

    def update(self, capital):
        cursor = self.db.cursor()
        sql = "update capitals set name = %s, country = %s, population = %s where id = %s"
        values = [
            capital['name'],
            capital['country'],
            capital['population'],
            capital['id']
        ] 
        cursor.execute(sql, values)
        self.db.commit()
        return capital

    def delete(self, id):
        cursor = self.db.cursor()
        sql = "delete from capitals where id = %s"
        values = [id]
        cursor.execute(sql, values)
        self.db.commit()
        print("Delete done") 

    def convertToDict(self, result):
        colnames = ['id', 'name', 'country', 'population']
        capital = {}
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                capital[colName] = value
        return capital

capitalDAO = CapitalDAO()