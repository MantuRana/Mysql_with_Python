import mysql.connector

# connectivity

# mycon = mysql.connector.connect(host="localhost",user="root",passwd="")
# if mycon.is_connected():
#     print("successfully")

# create database
# connection = mysql.connector.connect(host="localhost",user="root",passwd="")
# cur = connection.cursor()
# cur.execute("Create database pythondatabase")
# print(" create database successfully")


# #      create table
# connection = mysql.connector.connect(host="localhost",user="root",passwd="",database="pythondatabase")
# query = "CREATE TABLE PYTHON(bookid integer(5),Books varchar(20),price float(5,3))"
# cur = connection.cursor()
# cur.execute(query)
# print("successfully")

#       # insert data
# connection = mysql.connector.connect(host="localhost",user="root",passwd="",database="pythondatabase")
# query = "insert into PYTHON(bookid,Books,price)values(%s,%s,%s)"
# b1 = (101,"c++",1200)
# cur = connection.cursor()
# cur.execute(query,b1)
# connection.commit()
# print("insert successfuly")


#       #     insert many data

# connection = mysql.connector.connect(host="localhost",user="root",passwd="",database="pythondatabase")
# query = "insert into PYTHON(bookid,Books,price)values(%s,%s,%s)"
# books = [(101,"java",100),(101,"Programming",102),(101,"python",104),(101,"php",104)]
# cur = connection.cursor()
# cur.executemany(query,books)
# connection.commit()
# print("success")


# fetch all data from database
# mycon = mysql.connector.connect(host="localhost",user="root",passwd="",database="pythondatabase")
# query = "select * from PYTHON"
# cur = mycon.cursor()
# cur.execute(query)
# result = cur.fetchall()
# for x in result:
#     print(x)
    
# update records

# mycon = mysql.connector.connect(host="localhost",user="root",passwd="",database="pythondatabase")
# str = "UPDATE PYTHON SET Books = 'Javascript',price=90  WHERE bookid = 101"
# cur = mycon.cursor()
# cur.execute(str)
# mycon.commit()

# # DELETE RECORDS FROM TABLE

# mycon = mysql.connector.connect(host="localhost", user="root", passwd="", database="pythondatabase")
# str = "DELETE from PYTHON WHERE Books ='c++'"
# cur = mycon.cursor()
# cur.execute(str)
# mycon.commit()