import mysql.connector

#myconn = mysql.connector.connect(host='localhost', user='root', password='sumit7397', database='student')

cur = myconn.cursor()  # To build a Connection with MySQL

query = "INSERT INTO student(Stu_id, Stu_name, joining_date, Address) values(%s, %s, %s, %s)"
val = [(101, "Arpita", '2014-08-13', 'BGNagar'),
       (102, 'Leela priya', '2014-06-14', 'Eluru'),
       (103, 'Moksha Prada', '2016-07-15', 'Hyderabad')]


cur.executemany(query, val)

myconn.commit()

myconn.close()
