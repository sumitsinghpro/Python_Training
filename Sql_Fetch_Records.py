import mysql.connector

#myconn = mysql.connector.connect(host='localhost', user='root', password='sumit7397', database="student")

cur = myconn.cursor()  # To build a Connection with MySQL

query = "SELECT * FROM student"

cur.execute(query)

my_result = cur.fetchall()

for x in my_result:
    print(x)

myconn.close()
