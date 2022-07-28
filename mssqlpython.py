#MSSQL 
#importing pyodbc module
from random import random
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


#dunder methods
#to view availble dunder methods in a class use dir() method

print(dir(int)) #int is object of predefined class
''
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', 
'__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', 
'__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', 
'__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', 
'__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', 
'__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 
'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes'] 
''
#all of these r dunder methods that we can use with int class obj

#dunder __repr__()
class Car:
    pass
car=Car()
print(car) #prints the mem addr of obj car

#to change the behaviour of __repr__ ()override it in the class!!
class Car:
    def __repr__(self):#override __repr__() so this stmt gets priority
        return f"{self.__class__.__qualname__}"

car=Car()
print(car) #Car

class Car:
    def __str__(self):
        return f"{self.__class__.__qualname__}"

car=Car()
print(car.__str__())

#math dunder
class randomnumbers:
    def __init__(self,a,b):
        self.a=a
        self.b=b
#obj for randomno class
obj_a=randomnumbers(3,5)
obj_b=randomnumbers(6,8)

#adding the two obj
print(obj_a + obj_b)#cant add two objs
#TypeError: unsupported operand type(s) for +: 'randomnumbers' and 'randomnumbers'

#__add__() dunder
class randomnumbers:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    #override __add__()
    def __add__(self,other):#other is obj passing to this method
        #returns sum of two left and right digits converted to rand no obj
        return randomnumbers(other.a + self.a, other.b + self.b)

    def __repr__(self):
        return f"{self.__class__.__qualname__}({self.a},{self.b})"

obj_a=randomnumbers(3,5)
obj_b=randomnumbers(6,8)

print(obj_a + obj_b) #randomnumbers(9,13)
'''
#eg 2 dunder with class objects
class softwares:
    names=[]
    versions={}#holds key value pair
    #overriding constructor
    def __init__(self,name):
        if name:
            self,name=name.copy()#creates copy of list
        for names in name:
            self.versions[names]=1#initialize sw ver to 1
        else:
            raise Exception("names cant be empty")
               
#overriding 
    def __str__(self):
        s="list of sw and versions"
        for key,value in self.versions.items():
            s+= f"{key}:{value}\n"
        return s
    #overriding __setitem__ dunder
    def __setitem__(self,name,version):#invoked when 
        if name in self.versions:
            self.versions[name]=version
        else:
            raise Exception("sw name doesnt exist")

    #overriding __getitem__ dunder
    def __getitem__(self,name):
        if name in self.versions:
            return self.versions[name]
        else:
            raise Exception("sw name doesnt exist")
    
    #overriding __delitem__ dunder
    def __delitem__(self,name):
        if name in self.versions:
            del self.versions[name]#delete item frm dict versions
            self.names.remove(name)

    #overriding __len__ dunder
    def __len__(self):
        return len(self.names)

    #overriding __contains__ dunder
    def __contains__(self,name):
        if name in self.versions:
            return True
        else:
            return False


#ajmi
sw1 = softwares(['ps','msword','mspaint'])   
#print the softaware class object
print(sw1)
#trying to set a new version for ms word
sw1['msword'] = 2
print(sw1)

#trying to get a  version number for ms word
print(sw1['msword'])

#kripa
#creating sw class obj
sw1=softwares(['ps','msword','mspaint'])

#print sw class obj
print(sw1)
sw1['msword']=2
print(sw1)
#trying to get version no for msword
print(sw1['msword'])
del sw1['msword']#deleting item
print(len(sw1))#print len of sw1
if 'msword' in sw1:
    print("sw exists")
else:
    print("sw doesnt exist")

    