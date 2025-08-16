import mysql.connector

db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    
)
cursorobj=db.cursor()

cursorobj.execute('CREATE DATABASE elderco')

print("all done")
