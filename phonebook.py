import pyodbc
import re
conString='Driver={SQL Server};Server=DESKTOP-9FVJH8C\SQLEXPRESS;Database=phonebook_db;Trusted_Connection=yes;'

class Utils:
    def getNumber():
        value = input()
        return value

def initialiseContactsDB():
    try:
        print("Connecting to database..")
        myconn = pyodbc.connect(conString)
        myCursor = myconn.cursor()
        try:     
            myCursor.execute('''CREATE TABLE phonebook(
                id INT IDENTITY PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                phone VARCHAR(20) NOT NULL UNIQUE,
                )''')
        except Exception as e:
                print('Something went wrong')
                print(f"{type(e).__name__} was occured,")
    except:
        print("Could not connect to database")
    myconn.commit()
    myconn.close()

def searchByNumber():
    print("Enter Number: ")
    number = Utils.getNumber()
    while(True):
        try:
            print("Connecting to database..")
            myconn = pyodbc.connect(conString)
            myCursor = myconn.cursor()
            try:
                print("Searching contact from the database")
                myCursor.execute('SELECT * FROM phonebook WHERE phone = ?;',(number))           
            except Exception as e:
                print('Could not search from database')
                print(e)
            else:
                contact = myCursor.fetchall()
                if len(contact)>0:
                    print('Contact Found..')
                    for _, name, phone  in contact:
                        print(f'Name: {name}\nPhone: {phone}')
                else:
                    print('This number does not exist in database')
            break
        except:
            print("Could not connect to database")
            continue
    myconn.commit()
    myconn.close()


def addContact():
    name = input("Enter Name: ")
    print("Enter Phone Number: ")
    number = Utils.getNumber()
    while(True):
        try:
            print("Connecting to database..")
            myconn = pyodbc.connect(conString)
            myCursor = myconn.cursor()
            try:
                print("Adding contact to the database")
                myCursor.execute('INSERT INTO phonebook(name,phone) VALUES(?,?);',(name, number))           
            except Exception as e:
                print('Could not write to database')
                print(e)
            else:
                print('Contact added successfully..')
            break
        except:
            print("Could not connect to database")
            continue
    myconn.commit()
    myconn.close()
       

def listAllContacts():
    while(True):
        try:
            print("Connecting to database..")
            myconn = pyodbc.connect(conString)
            myCursor = myconn.cursor()
            try:
                print("Listing All Contacts from database")
                myCursor.execute('SELECT * FROM phonebook ;')           
            except Exception as e:
                print('Could not list data from database')
                print(e)
            else:
                contact = myCursor.fetchall()
                if len(contact)>0:
                    print('Contact are..')
                    for _, name, phone  in contact:
                        print(f'Name: {name}\nPhone: {phone}\n')
                else:
                    print('No contacts in database')
            break
        except:
            print("Could not connect to database")
            continue
    myconn.commit()
    myconn.close()

def searchByName():
    name = input("Enter Name: ")
    while(True):
        try:
            print("Connecting to database..")
            myconn = pyodbc.connect(conString)
            myCursor = myconn.cursor()
            try:
                print("Searching contact from the database")
                myCursor.execute('SELECT * FROM phonebook WHERE name = ?;',(name))           
            except Exception as e:
                print('Could not search from database')
                print(e)
            else:
                contact = myCursor.fetchall()
                if len(contact)>0:
                    print('Contact Found..')
                    for _, name, phone  in contact:
                        print(f'Name: {name}\nPhone: {phone}\n')
                else:
                    print('This name does not exist in database')
            break
        except:
            print("Could not connect to database")
            continue
    myconn.commit()
    myconn.close()

def deleteContact():
    print("Enter Number: ")
    number = Utils.getNumber()
    while(True):
        try:
            print("Connecting to database..")
            myconn = pyodbc.connect(conString)
            myCursor = myconn.cursor()
            try:
                print("Deleting contact from the database")
                myCursor.execute('DELETE FROM phonebook WHERE phone = ?;',(number))           
            except Exception as e:
                print('Could not delete from database')
                print(e)
            else:
                if myCursor.rowcount>0:
                    print('Contact deleted successfully..')
                else:
                    print('This number does not exist in database')
            break
        except:
            print("Could not connect to database")
            continue
    myconn.commit()
    myconn.close()

initialiseContactsDB()

st=1
while(st==1):
    print("""
    1. Add Contact
    2. List Contact
    3. Search by Name
    4. Search by Number
    5. Delete a number
    """)
    op = int(input("Enter your choice:"))
    match(op):
        case 1: addContact()
        case 2: listAllContacts()
        case 3: searchByName()
        case 4: searchByNumber()
        case 5: deleteContact()
        case _: print("Invalid option")

st=int(input("Do you want to enter another option?(1/0):"))