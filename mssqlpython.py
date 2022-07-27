#MSSQL 
#importing pyodbc module
import pyodbc

#create a connection string
constring="Driver={SQL Server};Server=DESKTOP-9FVJH8C\SQLEXPRESS;Database=emp_db;Trusted_Connection=yes;"

#connecting to db
connection=pyodbc.connect(constring)
'''
#get cursor obj
mycursor=connection.cursor()

#using cursor,execute sql command
mycursor.execute(''CREATE TABLE Emp_master3
(Id INT IDENTITY PRIMARY KEY,
	EmployeeCode VARCHAR(10),
	EmployeeName VARCHAR(25),
	DepartmentCode VARCHAR(10),
	LocationCode VARCHAR(10),
	Salary INT)'')

#for i in mycursor:
 #   print(i)

#commit connection and close
#used when making changes to db
connection.commit()
connection.close()

print("statement after the query")#there will be an error as the table is already created

#instead use try-except
try:
    mycursor=connection.cursor()

#using cursor,execute sql command
    mycursor.execute(''CREATE TABLE Emp_master3
    (Id INT IDENTITY PRIMARY KEY,
	EmployeeCode VARCHAR(10),
	EmployeeName VARCHAR(25),
	DepartmentCode VARCHAR(10),
	LocationCode VARCHAR(10),
	Salary INT)'')

except Exception as e:
    print("cant create table")
    print(e)

connection.commit()
connection.close()

print("statement after the query")

#using fetchall()
#gets all the data in db
try:
    mycursor=connection.cursor()
#using cursor,execute sql command
    mycursor.execute("SELECT * FROM Emp_master")

except Exception as e:
    print("cant read table")
    print(e)

#for row in mycursor.fetchall():
#   print(row)

#or dictionary that can be easily processed
emp=[{'empcode':row[1],'empname':row[2]}for row in mycursor.fetchall()]
print(emp)#it prints only the specified attributes in dict format

connection.close()


try:
    mycursor=connection.cursor()
#using cursor,execute sql command
    mycursor.execute("INSERT INTO Emp_master VALUES('E0008','arjun','IT','TVM',9000)")

except Exception as e:
    print("cant read table")
    print(e)

#for row in mycursor.fetchall():
#   print(row)

#or dictionary that can be easily processed
emp=[{'empcode':row[1],'empname':row[2]}for row in mycursor.fetchall()]
print(emp)#it prints only the specified attributes in dict format

connection.close()

#user raising exception using raise()
x=0
if x==0:
    raise Exception("no cant be zero")

x="hello"
if not type(x) is int:
    raise TypeError("int values are allowed")
'''

#creating user-defined exception class
#exceptions shld be derived frm built-in exceptions

class myerror(Exception):
    def __init__(self,value):#constructor
        self.value=value

    def __str__(self):
        return(repr(self.value))

try:
    x=0
    if x==0:
        raise(myerror("no cant be zero"))
except myerror as error:
    print("a new exception occured",error.value)

#exception class derived by another class
class myerror(Exception):
    pass

class  dividebyzero(myerror):
    pass
try:
    x=0
    if x==0:
        raise(myerror("no cant be zero"))
except myerror as error:
    print("a new exception occured",error.value)


    