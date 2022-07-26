""" 
#file handling
files=open("myfile.txt","r")#read
#print(files.read())#reads the whole file

#reading specified no of char
#print(files.read(10))#Jack and J

#reading a line frm txtfile
print(files.readline())#Jack and Jill 


#higher order function
def greet(name):
    return "Hello {}".format(name)

#define higher order func that accepts func
def print_greetings(fn,para):
    print(fn(para))

#calling higher order fn
print_greetings(greet,"kripa")

#map
def mapfn(a):
    return a*a

x=map(mapfn,(1,2,3,4))
#x is map obj need to convert into set/tuple
print(tuple(x))#(1,4,9,16)

#lambda fn
x=map(lambda x:x*x,(1,2,3,4))
print(tuple(x))#(1,4,9,16)

#filter func
def filterfn(x):
    if x>=3:
        return x

#calling filter fn
y=filter(filterfn,(1,2,3,4))
print(list(y))#[3,4]

#filter with lambda
y=filter(lambda x:(x>=3),(1,2,3,4))
print(list(y))#[3,4]

#reduce fn
from functools import reduce

x=reduce(lambda a,b:a+b,(23,21,45,98))
print(x)#187

#class and regular func without abstract class
class Lion:
    def feed_lion(self):
        print("Feeding a lion with raw meat")

class Panda:
    def feed_panda(self):
        print("Feeding a panda with bamboo")

class Snake:
    def feed_snake(self):
        print("Feeding a snake with mice")

#create obj for animals
simba=Lion()
po=Panda()
kingcobra=Snake()

#calling feeding fn
simba.feed_lion()
po.feed_panda()
kingcobra.feed_snake()


#importing abstract class and decorator
from abc import ABC, abstractmethod
#declaring abstract base class inheriting frm ABC
class Animal(ABC):
    @abstractmethod #deco for abstract method
    def feed(self):
        pass #placeholder to escape empty fn error

class Lion(Animal):
    def feed(self):
        print("Feeding a lion with raw meat")

class Panda(Animal):
    def feed(self):
        print("Feeding a panda with bamboo")

class Snake(Animal):
    def feed(self):
        print("Feeding a snake with mice")

simba=Lion()
po=Panda()
kingcobra=Snake()

simba.feed()
po.feed()
kingcobra.feed()

#instead of calling methods separately implement for loop
zooclasslist=[Lion(),Panda(),Snake()]
for animal in zooclasslist:
    animal.feed()


#abstract classes with para
from abc import ABC, abstractmethod
#declaring abstract base class inheriting frm ABC
class Animal(ABC):
    @abstractmethod #deco for abstract method
    def feed(self):
        pass #placeholder to escape empty fn error
   
    def do(self,action):#abstract method with para
        pass

class Lion(Animal):
    def feed(self):
        print("Feeding a lion with raw meat")
    def do(self,action,time):
        print(f"{action} a lion with raw meat at {time}")

class Panda(Animal):
    def feed(self):
        print("Feeding a panda with bamboo")
    def do(self,action,time):
        print(f"{action} a panda with bamboo at {time}")

class Snake(Animal):
    def feed(self):
        print("Feeding a snake with mice")
    def do(self,action,time):
        print(f"{action} a snake with mice at {time}")

simba=Lion()
po=Panda()
kingcobra=Snake()

zooclasslist=[Lion(),Panda(),Snake()]
for animal in zooclasslist:
    animal.feed()
    animal.do(action="Feeding", time="10:10 am")


#defining a diet property using property deco and abstract method
from abc import ABC, abstractmethod
#declaring abstract base class inheriting frm ABC
class Animal(ABC):
    @abstractmethod #deco for abstract method
    def feed(self):
        pass #placeholder to escape empty fn error
    
    #defining a diet property using property deco and abstract method
    @property
    @abstractmethod
    def diet(self):
        pass

    @property
    def food_eaten(self):#getter for food_eaten
        return self._food 
    
    #setter for food_eaten
    @food_eaten.setter#setter name same as method
    def food_eaten(self,food):
        if food in self.diet:
            self._food=food
        else:
            raise ValueError(f"this animal doesnt eat it")
    
    def do(self,action):#abstract method with para
        pass

class Lion(Animal):
    @property
    def diet(self):
        return["antelope","cheetah","buffalo"]

    def feed(self):
        print(f"Feeding a lion with {self.food_eaten}")

    def do(self,action,time):
        print(f"{action} a lion with raw meat at {time}")

class Panda(Animal):
    @property
    def diet(self):
        return["bamboo","leaves"]

    def feed(self):
        print(f"Feeding a panda with {self.food_eaten}")

    def do(self,action,time):
        print(f"{action} a panda with bamboo at {time}")

class Snake(Animal):
    @property
    def diet(self):
        return["mice","rabbit"]

    def feed(self):
        print(f"Feeding a snake with {self.food_eaten}")

    def do(self,action,time):
        print(f"{action} a snake with mice at {time}")

simba=Lion()
simba.food_eaten="buffalo"
simba.feed()
po=Panda()
po.food_eaten="bamboo"
po.feed()
kingcobra=Snake()
kingcobra.food_eaten="leaves"
kingcobra.feed()
''
Feeding a lion with buffalo
Feeding a panda with bamboo
ValueError: this animal doesnt eat it
''

#opening file cursor in read mode
myfile=open("myfile.txt","r")
#read all lines and return as list
filecontentslist=myfile.readlines()
print(filecontentslist)
myfile.close()

#append mode
myfile=open("myfile.txt","a")
myfile.write("\nHumpty Dumpty sat on a wall")
myfile.close()

#write mode
myfile=open("myfile.txt","w")
myfile.write("Humpty Dumpty sat on a wall\n")
myfile.close()

#checking pos of file ptr
myfile=open("myfile.txt","r")
print("file ptr now at",myfile.tell())#before reading

filecontentslist=myfile.readlines()
print("file ptr now at",myfile.tell())#after reading
print(myfile.readline())
''
myfile.seek(10)
print("file ptr now at",myfile.tell())
filecontentslist=myfile.readlines()
print("file ptr now at",myfile.tell())
print(filecontentslist)
myfile.close()

#renaming a file 
import os
from sndhdr import whathdr
if os.path.exists("myfile.txt"):
    os.rename("myfile.txt","mynewfile.txt")
    print("rename success")
else:
    print("File doesnt exist")

#to create new directory 
#os.mkdir("mydir")

#to display cwd
print(os.getcwd()) #C:\Users\kripa\Camp2\PythonInAppDemo

#to change cwd
#os.chdir("mydir")
print(os.getcwd()) #C:\Users\kripa\Camp2\PythonInAppDemo\mydir

#to delete directory 
#os.rmdir("mydir")

#to go back the previous directory
#(os.chdir("..")
print(os.getcwd())

#to list all files and folders
result = os.listdir(os.getcwd())
print(result)

#write output of a program into a file.
#check_call() : from module subprocess to executea python script and write the output of that script to a file
#one python file executes the script file.py and writes its output to the text file sample.txt with will automatcally close file pointer once completed
#for that run an external python file(fileoutputsave.py) and save its results to another file as txt
import subprocess
with open("sample.txt", "wb") as f:
    subprocess.check_call(["python","fileoutputsave.py"], stdout=f)


#exception handling
try:
    div=4//0
    print(div)
except ZeroDivisionError:
    print("dividing by zero not possible")
except:
    print("error")
finally:
    print("will never give up")

#formatting exception msg
try:
    div=4//2
    print(div)
except Exception as e:
    print("dividing no by 0")
    print(f"{type(e).__name__} has occured. More details below:")
    print(e) #prints details of exception
else:#including else; stmt executes if try is successful
    print("division completed and result =",div)
finally:
    print("will never give up")

#nested try-except
try:
    f=open("mynewfile.txt") #opens file
    try:#if file can be created then execute this
        f.write("Ola!")
    except:#if writing cant happen
        print("cant write the file")
    finally:
        f.close()
except:#for file creation 
    print("File cant be opened")

"""


