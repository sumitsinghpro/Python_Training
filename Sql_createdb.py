import mysql.connector



#myconn = mysql.connector.connect(host='localhost', user='root', password='sumit7397')



cur = myconn.cursor()  # To build a Connection with MySQL



query = "CREATE DATABASE travel"





cur.execute(query)



query2 = "show databases"



cur.execute(query2)



for x in cur:
   print(x)



myconn.close()
 