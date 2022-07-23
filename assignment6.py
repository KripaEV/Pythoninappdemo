#1. Number guessing game
import random 
    
def game(): 
    comp_choice=random.randint(1,10)
    print("I've already guessed one")
    flag=0
    diff=0
    for i in range(5):
        print("Attempt",i+1)
        num=int(input("Enter your guess:"))
        diff=abs(num-comp_choice)
        if(diff==9 or diff==8):
            print("Your guess is very cold. Try again")
        elif(diff==7 or diff==6):
            print("Your guess is cold. Try again")
        elif(diff==5 or diff==4):
            print("Your guess is neutral. Try again")
        elif(diff==3):
            print("Your guess is warm. Try again")
        elif(diff==2 or diff==1):
            print("Your guess is hot. Try again")
        else:
            flag=1
            break 
    if (flag==1):
        print("Its a match! Congrats!")
    else:
        print("You lost! The guess was",comp_choice)


print('''1.Start the game
2. Exit''')
ch=int(input("Enter your choice:"))
if(ch==1):
    game()
else:
    exit()

op=1
while(op==1):
    print('''1. Play again
2. Exit''')
    op=int(input("Enter your choice:"))
    if(op==1):
        game()
    else:
        exit()

#2. Student report card mngt system
class student:
    def __init__(self,name,math,phy,chem,eng,pgmg):
        self.__name=name
        self.__math=math
        self.__phy=phy
        self.__chem=chem
        self.__eng=eng
        self.__pgmg=pgmg

    def display(self):
        print('Name :', self.__name)
        print('Marks:')
        print('Maths:', self.__math)
        print('Physics:', self.__phy)
        print('Chemistry:', self.__chem)
        print('English:', self.__eng)
        print('Programing:', self.__pgmg)

class studentmngtdb:
    stu=dict()
    def create():
        rollno=int(input("Enter the roll number:"))
        name=input("Enter the name:")
        print("Enter the marks")
        math=int(input("Maths:"))
        phy=int(input("Physics:"))
        chem=int(input("Chemistry:"))
        eng=int(input("English:"))
        pgmg=int(input("Programming:"))
        stud=student(name,math,phy,chem,eng,pgmg)
        studentmngtdb.stu[rollno]=stud
        print("Record added")

    def delete():
        rno=int(input("Enter the roll number of the record to be deleted:"))
        if studentmngtdb.stu.get(rno):
            del studentmngtdb.stu[rno]
            print("Record deleted")
        else:
            print("Record doesnt exist")
    
    def modify():
        rno=int(input("Enter the roll number of the record to be modified:"))
        if studentmngtdb.stu.get(rno):
            stud=studentmngtdb.stu.get(rno)
            op=1
            while(op==1):
                opt=int(input('''Choose the mark to modify
            1.Math
            2.Physics
            3.Chemistry
            4.English
            5.Programming
            Choice:'''))
                if(opt==1):
                    stud.math=int(input("Maths:"))
                elif(opt==2):
                    stud.phy=int(input("Physics:"))
                elif(opt==3):
                    stud.chem=int(input("Chemistry:"))
                elif(opt==4):
                    stud.eng=int(input("English:"))
                elif(opt==5):
                    stud.pgmg=int(input("Programming:"))
                else:
                    print("Invalid input")
                op=int(input("Do you want to modify more marks?(0/1)"))
        else:
            print("Record doesnt exist")
    
    def displayall():
        num=len(studentmngtdb.stu)
        if(num>0):
            print("Student details-")
            for rollno, stud in studentmngtdb.stu.items():
                print("\nRollno:",rollno)
                stud.display()
        else:
            print("No records")
    
    def displayrec():
        rno=int(input("Enter the roll number of the record to be displayed:"))
        if studentmngtdb.stu.get(rno):
            print("\nRollno:",rno)
            studentmngtdb.stu[rno].display()
        else:
            print("Record doesnt exist")



op='y'
while(op=='y'):
    print('''1. Create a record
2. Delete a record
3. Modify marks
4. Display all records
5. Display a student record''')
    ch=int(input("Enter your choice:"))
    if(ch==1):
        studentmngtdb.create()
    elif(ch==2):
        studentmngtdb.delete()
    elif(ch==3):
        studentmngtdb.modify()
    elif(ch==4):
        studentmngtdb.displayall()
    elif(ch==5):
        studentmngtdb.displayrec()
    else:
        print("Invalid input")
    op=input("Do you want to enter another choice?(y/n)")