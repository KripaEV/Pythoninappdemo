import os
import re

#to list all contacts in alphabetical order
def list():
    lst=[]
    newLst=[]
    try:
        f=open('contacts\contacts.txt', 'r')
        for line in f:
            lst.append(line)
        for i in lst:
            if i != 'Name - Phone Number\n':
                newLst.append(i.strip())
        newLst.sort()
        for i in newLst:
            print(i)
    except:
        print("Unsuccessful")

def addcontact():
    name=input("Enter the name of new contact: ")
    num=input("Enter the phone number: ")
    try:
        file=open("contacts\contacts.txt", "a")
        filecontactlist=name + " - " + num
        file.write(filecontactlist)
        file.write("\n")
        file.close()
        print("Added Successfully")
    except:
        print("Unsuccessful")
    print("\nUpdated PhoneBook is: ")
    print(list())


def deletecontact():
    flag=0
    name = input("Enter the name of contact to delete: ")
    try:
        file1=open("contacts\contacts.txt","r")
        line=file1.readlines()
    
        file2=open('contacts\contacts.txt', 'w')
        for l in line:
            n,phone=l.strip().split('-')
            if n.strip()==name:
                print("Contact deleted successfully")
                continue
            file2.write(l)
                    
    except:
        print("Unsuccessful")
    print("\nUpdated PhoneBook is: ")
    list()


def searchName():
    name = input("Enter the name of contact to search: ")
    flag=False
    try:
        file1=open("contacts\contacts.txt", "r")
        line= file1.readlines()
        for l in line:
            n,phone=l.strip().split('-')
            if n.strip()==name:
                print('Name - Phone Number\n', l)
                print("Contact found")
                flag=True
        if not flag:
            print("Not found")

    except:
        print("Unsuccessful")
        
#to search a contact by number
def searchno():
    flag=False
    num = input("Enter the phone number to search: ")
    try:
        file1=open("contacts\contacts.txt", "r")
        line= file1.readlines()
        for l in line:
            n,phone=l.strip().split('-')
            if phone.strip()==num:
                print('Name - Phone Number\n', l)
                print("Contact found")
                flag=True
        if not flag:
            print("Not found")
    except:
        print("Unsuccessful")

def accept():   
    while(True):
        ch =int(input("""
    1.List all contacts
    2.Add a new contact
    3.Delete a contact
    4.Search by name
    5.Search by number
    6.Exit
    Enter the choice: 
    """))
        if ch == 1:
            print("List all contacts")
            list()
        elif ch == 2:
            print("Add a new contact")
            addcontact()
        elif ch == 3:
            print("Delete a contact")
            deletecontact()
        elif ch == 4:
            print("Search by name")
            searchName()
        elif ch == 5:
            print("Search by number")
            searchno()
        else:
            print("Invalid Input. Try Again!")

#print(os.getcwd())
if os.path.isdir("contacts") == True:
    if os.path.exists("contacts\contacts.txt"):
        accept()
    else:
        myFilePtr = open("contacts\contacts.txt","w")
        with open("contacts\contacts.txt", "a") as f:
            f.write("Name - Phone Number\n")
else:
    os.mkdir("contacts")