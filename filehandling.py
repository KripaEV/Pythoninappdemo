import os
result = os.listdir(os.getcwd())
print(result)

#os.mkdir("Contacts")

if os.path.exists("contacts.txt"):
    print("File 'contacts.txt' exists")
else:
    file=open("contactsfile.txt","a+")
    print("File successfully created")
    file.close()

#fcont=dict()

def listcontacts():
    file=open("contacts.txt","r")
    filecontentslist=file.readlines()
    filecontentslist.sort()
    print(filecontentslist)
    file.close()

def addcontact():
    file=open("contacts.txt","a")
    filecontact=input("Enter the name and number:")
    file.write(filecontact)
    print("Contact successfully added")
    file.write("\n")
    file.close()

def namesearch():
    name=input("Enter the name of contact to search:")


#def nosearch():

def deletecontact():
    file=open("contacts.txt","r")
    file2=open("temp.txt","w")
    name=input("Enter the name of contact to delete:")
    file.write(name)
    for line in file:
            if line.strip("\n").startswith(name):
                file2.write(line)
    print("Contact successfully deleted")
    os.remove("temp.txt")
    file2.close()
    file.close()
    

st=1

while(st==1):
    print('''1.List all contacts
2.Add a new contact
3.Search a new contact
4.Search by number
5.Delete a contact''')
    ch=int(input("Enter your choice:"))
    match(ch):
        case 1:listcontacts()
        case 2:addcontact()
        case 3:namesearch()
        #case 4:nosearch()
        #case 5:deletecontact()


import os
import re

#to list all contacts in alphabetical order
def listcontacts():
    list1=[]
    list2=[]
    try:
        file=open("contacts\contacts.txt", 'r')
        for line in file:
            list1.append(line)
        for i in list1:
            if i != 'Name - Phone Number\n':
                list2.append(i.strip())
        list2.sort()
        for i in list2:
            print(i)
    except:
        print("Error")

def addcontact():
    name=input("Enter the name of new contact: ")
    num=input("Enter the phone number: ")
    try:
        file=open("contacts\contacts.txt", "a")
        filecontactlist= name + " - " + num
        f.write(filecontactlist)
        f.write("\n")
        f.close()
        print("Added Successfully")
    except:
        print("Unsuccessful")
    print("\nUpdated PhoneBook is: ")
    list()


def deletecontact():
    flag=0
    name = input("Enter the name of contact to delete: ")
    try:
        file1=open("contacts\contacts.txt", "r")
        line=file1.readlines()
    
        file2=open('contacts\contacts.txt', 'w')
        for l in line:
            if l.find(name)==-1:
                file2.write(l)
                    
    except:
        print("Unsuccessful")
    print("\nUpdated PhoneBook is: ")
    list()


def searchName():
    name = input("Enter the name of contact to search: ")
    try:
        file1=open("contacts\contacts.txt", "r")
        line= file1.readlines()
    
        file2=open('contacts\contacts.txt', 'r')
        for l in line:
            if l.find(name) != -1:
                print('Name - Phone Number\n Contact: ', l)

    except:
        print("Unsuccessful")
        
#to search a contact by number
def searchno():
    num = input("Enter the phone number to search: ")
    try:
        file1=open("contacts\contacts.txt", "r")
        line= file1.readlines()
    
        file2=open('contacts\contacts.txt', 'r')
        for l in line:
            if l.find(num) != -1:
                print('Name - Phone Number\n Contact: ', l)
    except:
        print("Unsuccessful")

#choice selection
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
