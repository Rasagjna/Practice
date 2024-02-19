# import mysql.connector
# mydb = mysql.connector.connect(host="localhost",user="root",password="K_L_S_r444",database="example")
# mycursor=mydb.cursor()
# mycursor.execute("select * from student")
# result=mycursor.fetchone()
# # print(result)
# print(mycursor)
# //////////////////////////////////
import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='example',
                                         user='root',
                                         password='K_L_S_r444')
    sql_select_Query = "select * from Laptop"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in Laptop is: ",
          cursor.rowcount)
    print("All fetched records = ", records)  # list of tuple records
    print("\nPrinting each laptop record")
    print(records
          )
    for row in records:
        print(row)
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Price = ", row[2])
        print("Purchase date = ", row[3], "\n")
except Error as e:
    print("Error reading data from MySQL table", e)
