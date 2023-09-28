import mysql.connector

dataBase  = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
)

#prepare a cursor object

cursorObject = dataBase.cursor()

#Criar a base de dados

cursorObject.execute("CREATE DATABASE elderco")

print("All Done!!")
