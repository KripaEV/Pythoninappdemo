from abc import ABC
from operator import truediv
import sys
"""
#print("Hello World")
#print(sys.version)

#learning to comment
#print("{} is my country. All Indians are my brothers and sisters".format('India'))
#print("India is my country. All Indians are my brothers and sisters".count('India'))
#mystring="Superman"
#print(mystring.endswith('man'))
#print(mystring.endswith('man',3))
#print(mystring.endswith(('man','ma'),2,6))

mystring2="Good morning"
print(mystring2.find('Go'))
#test check 1,2,3

#tuples in python
months=("Jan","Feb","Mar")
print(months[0])
print(months[-1])
print(len(months))
print("Jan" in months)
#del(months)
print(months)#NameError: name 'months' is not defined
print(months+months)
print("ORA "*10)

#dictionary 
#method 1
students={"ABC":12,"DEF":14,"JKL":13}
#method 2
students=dict(ABC=12,DEF=14,JKL=13)
#method 3
students=dict({"ABC":12,"DEF":14,"JKL":13})

print(students)

#dict func
print(students.get("JKL"))#returns correspoing value
print(students.items())#returns dict items as array of tuples
print(students.keys())#returns key of dict
print(students.values())#return values of dict
print("DEF" in students)#check if key is present
print(14 in students.values())#check if value is present
print(len(students))

students2={"GHI":15,"XYZ":16}
students.update(students2)#adds the new val to old dict
print(students)

students.clear() #clears items
print(students)
del students #del dict
print(students)

#set
months={"Jan","Feb","Mar"}
print(months)
print(type(months))

for i in months:
    print(i)

#declare an empty set
days=set()
#add values to set
days.add("Mon")
days.add("Tue")
days.add("Wed")
days.update(["Thu","Fri"])
#if [] not present in update() o/p will come as ind letters

days.discard("Thu")#remove items but doesnt show error if not present
#days.remove("Thu")#remove items but shows error if not present
for day in days:
    print(day)
#clear elt in set
days.clear()

#set operations
months={"Jan","Feb","Mar"}
months2={"Apr","May","Mar"}
months4={"Mar","Apr","Jun","Jul"}

#union operation
months3=months|months2
print(months3)
for month in months:
    print(month)

#intersection
months3=months&months2
print(months3)

#intersect update
#months.intersection_update(months2,months4)
#print(months)

#diff
months3=months-months2
print(months3)

#symmetric diff-all elt except common ones
months3=months^months2
print(months3)

#set comparison
months={"Jan","Feb","Mar","Apr","May","Jun"}
months2={"Apr","May","Mar"}
months3={"Mar","Apr","Jun","Jul"}

#check if months is superset of months2
print(months>months2)
#equal(no of elt and elts shld be same)
print(months3==months2)
#equal and month is superset of month2
print(months>=months2)

#frozen set
frozenmonth=frozenset(["Nov","Dec"])#immutable set
print(type(frozenmonth))
print(frozenmonth)
frozenmonth.add("Oct")


#i/p and o/p func
studentname=input("Enter your name: ")
studentage=input("Enter your age: ")
print(studentname)
print(type(studentname))
print(studentage)
print(type(studentage))

#diff print stmt
print("The name is",studentname,"and the age is",studentage)
print("The name is %s and the age is %s"%(studentname,studentage))
print("The name is {} and the age is {}".format(studentname,studentage))

#print in multiple lines
print('''Hello World
How are you?''')

#print a new line
print("Hello\nhow are you?")
print("I'm 5\'3\"")


#conditional stmt
#if
num=input("Enter 1 or 2:")
if num=='1' :
    print("Num entered is 1")
elif num=='2':
    print("Num entered is 2")
else:
    print("Invalid no")

#inline if stmt
b=12
a=12 if b==10 else 13
print(a)

print("b is ten" if b==10 else "b is not 10")


#switch or match case stmt
#func def
def http_status(status):
    match(status):
        case 400:
            return "Bad request"
        case 404:
            return "pg not found"
        case _: 
            return "unknown error"

#calling func inside print stmt
print(http_status(404))


#loop
#for
fruits=['apples','mango','strawberry']
for fruit in fruits:#without index, just the item
    print(fruit)

for index,fruit in enumerate(fruits):#for index value
    print(index,fruit)

#while
ctr=5
while ctr>0:
    print("ctr = ",ctr)
    ctr=ctr-1

#break
j=0
for i in range(10):
    j=j+2
    print('i=',i,'j=',j)
    if(j==6):
        break

#continue
j=0
for i in range(10):
    j=j+2
    print('i=',i,'j=',j)
    if(j==6):
        continue
    print('j value is:',j)

#try and except
try:
    answer=12/0
    print(answer)
except:
    print("Some friendly error msg")

#funcs
def checkifprime(num):
    for x in range(2,num):
        if(num%x==0):
            return True
        return False
print(checkifprime(15))#false

def calculation(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a%b
    return(add,sub,mul,div)

output=calculation(4,5)
print("Add result",output[0])
print("Sub result",output[1])
print("Mul result",output[2])
print("Div result",output[3])

#demonstrating variable scope
msg="Global var"#global var

def myfunction():
    global msg #enable global var
    print("inside function")
    print(msg)
    msg2="Local var"
    print(msg2)

myfunction()


#passing list of arg into func
def make_pizza(size,*toppings):
    print(f"\nMaking a {size}-inch pizza wih foll toppings:")
    for top in toppings:
        print(f"{top}")
make_pizza(12,"mozzarella")
make_pizza(16,"pepperoni","mushrooms","olive")


#lambda func 
sum=lambda a,b:a+b
print("sum of two num",sum(2,3))

#importing a module
import random as r
print(r.randrange(1,10))

#random built in module
import random
print(random.random())
print(random.randint(5,20))
print(random.choice(["head","tail"]))

myshirt=["blue","red"]
random.shuffle(myshirt)
print(myshirt)

random.seed(100)
print(random.random())

import datetime
print(datetime.datetime.now())

#creating custom datetime obj
birthday=datetime.datetime(2022,7,18)
print(birthday)

#time comparison
from datetime import datetime as dt

if dt(dt.now().year,dt.now().month,dt.now().day,9)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,18):
    print("Works")
else:
    print("shift completed")

#calling the custom module created
import prime

ans=prime.checkifprime(10)
print(ans)


#rights of a func to the right of var
#1.assigning func to var
def func():
    print("This is a func")

myfunc=func
func()
myfunc()

#2.pass func as arg to another func
def func2(recfn):
    recfn()
    recfn()
func2(func)

#3. return frm another func
def return_to_upper_fn():
    return str.upper

upperref=return_to_upper_fn()

#4.def func inside other func
def outer():
    print("Outer func")

    def firstinner():
        print("First inner func")

    def secondinner():
        print("Second inner func")
    
    firstinner()
    secondinner()

#5.inner func can access enclosing func var
def Outer(greeting):
    print("Outer func:",greeting)

    def firstinnerfn():
        print("first inner func:",greeting)
    
    return firstinnerfn

outerfuncvar=Outer("Peace")
outerfuncvar()


#decorator
def mydecorator(func):
    def innerwrapper():
        print("just before the received fn call")
        func()
        print("just after received fn call")
    return innerwrapper

#def sample fn to pass to decorator
def decofnpass():
    print("Simple func to pass into deco")

mydecodemo=mydecorator(decofnpass)
mydecodemo()

#syntactic sugar
@mydecorator
def newdecofnpass():
    print("A new simple fn to pass into decorator")

newdecofnpass()

#class constructor
#creating class
class employee:
    'common base class for all employees'
    #defining a global variable or data member
    empcount = 0 
    def __init__(self, name, salary): 
        self.name = name #can call across the class
        self.salary = salary 
        employee.empcount += 1 
    
    #define a simple member function
    def displayempcount(self): 
        print("Employee Count: ", employee.empcount) 
    def displayempdetails(self): 
        print("Name: ", self.name) 
        print("Salary: ", self.salary)

#create an object of employee class
employee1 = employee("Tom", 2000)
employee1.displayempcount() 

employee2 = employee("Jerry", 3000)
employee2.displayempcount()

#call function using dot operator (object)
employee1.displayempcount()
employee2.displayempcount()
employee1.displayempdetails()
employee2.displayempdetails()

print("Total number of Employee : ", employee.empcount)

#inheritance
class rocket:
    def __init__(self,name,dist):
        self.name=name
        self.dist=dist
        self.__myprivatevar="test"
    def launch(self):
        return "%s has reached %s"%(self.name,self.dist)
    
class marsrover(rocket):#derived class
    def __init__(self,name,dist,maker,vehiclecode):
        rocket.__init__(self,name,dist)
        self.maker=maker
        #defining a private variable
        self.__vehiclecode=vehiclecode
    def printmaker(self):
        return "%s launched by %s"%(self.name,self.maker)
    def getvehiclecode(self):

    def getprivate(self):
        return self.__myprivatevar

#creating obj for rocket(main class)
x=rocket("small rocket","stratosphere")
y=marsrover("marsrover","till mars","ISRO",12345)

print(y._rocket__myprivatevar)
#somewhere here encapsulation is icluded
print(x.launch())
print(y.launch()) 
print(y.printmaker())
#print(y.__vehiclecode)#due to encapsulation, cant access private var
print(y.getvehiclecode())#correct way to access private var
"""
#its wrong and incomplete 
#polymorphism
"""
#decorator
def mydecorator(func):
    def innerwrapper():
        print("just before the received fn call")
        func()
        print("just after received fn call")
    return innerwrapper

#def sample fn to pass to decorator
def decofnpass():
    print("Simple func to pass into deco")

mydecodemo=mydecorator(decofnpass)
mydecodemo()

#syntactic sugar
@mydecorator
def newdecofnpass():
    '''sample doc string for mewdecofnpass() fn'''
    print("A new simple fn to pass into decorator")

newdecofnpass()
print(newdecofnpass.__name__)
help(newdecofnpass)

#passing arg in to decorator
def acceptdecorator(mystring3):
    def mydecorator(myfunc):
        @functools.wraps(myfunc)
        def innerwrapper(*args):#wrapper fn
            print("Just b4 the recieved fn call"+mystring3)
            myfunc(*args)
            print("Just after the received fn call")
            return myfunc(*args)
        return innerwrapper
    return mydecorator

@acceptdecorator
def newdecofnpass():
    '''sample doc string for mewdecofnpass() fn'''
    print("A new simple fn to pass into decorator")

newdecofnpass()
print(newdecofnpass.__name__)
help(newdecofnpass)

####decorators with classes
class Hero:
    #define the decorator @classmethod
    @classmethod
    def say_class_hello(cls):#class method receives ref as 
        if(cls.__name__=="Heroson"):
            print("Hi price, called from heroson")
        elif(cls.__name__=="Herodaughter"):
            print("Hi pricess, called from Herodaughter")
    #define the decorator @staticmethod
    @staticmethod
    def say_hello():
        print("Hello")
class Heroson(Hero):
    def say_son_hello(self):
        print("Hello son frm sub class Heroson")

class Herodaughter(Hero):
    def say_son_hello(self):
        print("Hello daughter frm sub class Herodaughter")
    
testHeroson=Heroson()
testHeroson.say_class_hello()
testHeroson.say_hello()

testHerodaughter=Herodaughter()
testHerodaughter.say_class_hello()
testHerodaughter.say_hello()

"""

class House:
    #constructor
    def __init__(self,price):
        self.__price=price#rpivate


    @property#getter method
    def price(self):
        return self.__price
    #using setter to access private member
    @price.setter
    def price(self,new_price):
        self.__price=new_price 
    
    @price.deleter
    def price(self):
        del self.__price
    
#typical access and update will be like this:
house = House(500000)#create obj
print(house.price) #access attributes
house.price=1000000 #modifying atrribute
print(house.price) #access attributes
del house.price #delete price of the house instance
print(house.price)
