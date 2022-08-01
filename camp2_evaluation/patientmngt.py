'''Q2. Create a Patient management system python console application that manages records of the patients in a hospital. 
You may use the MSSQL database'''

from multiprocessing import connection
import pyodbc

constring='Driver={SQL Server};Server=DESKTOP-9FVJH8C\SQLEXPRESS;Database=PMSystem;Trusted_Connection=yes;'

def initialiseDB():
    try:
        print("Connecting to database..")
        connection = pyodbc.connect(constring)
        mycursor = connection.cursor()
        try:     
            mycursor.execute('''CREATE TABLE phonebook(
                id INT IDENTITY PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                phone VARCHAR(20) NOT NULL UNIQUE,
                )''')
        except Exception as e:
                print('Something went wrong')
                print(f"{type(e).__name__} was occured,")
    except:
        print("Could not connect to database")
    connection.commit()
    connection.close()

def addPatientRec():
    

st=1
while (st==1):
    print("""
    1. Add Patient Record
    2. Update Patient Record
    3. Delete Patient Record
    4. Search and List Patient Record
    """)
    op = int(input("Enter your choice:"))
    match(op):
        case 1: addPatientRec()
        case 2: updatePatientRec()
        case 3: deletePatientRec()
        case 4: searchPatientRec()
        case _: print("Invalid choice")

st=int(input("Do you want to enter another option?(1/0):"))