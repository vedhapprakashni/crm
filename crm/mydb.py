import mysql.connector

db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Shivani2004*',
    
)
cursorobj=db.cursor()

cursorobj.execute('CREATE DATABASE elderco')

print("all done")