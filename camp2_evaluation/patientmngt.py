'''Q2. Create a Patient management system python console application that manages records of the patients in a hospital. 
You may use the MSSQL database'''

from dataclasses import dataclass
from multiprocessing import connection
import pyodbc
import functools

constring='Driver={SQL Server};Server=DESKTOP-9FVJH8C\SQLEXPRESS;Database=PMSystem;Trusted_Connection=yes;'

def database_connection(myFunc):
    @functools.wraps(myFunc)
    def innerWrapper(*args):
        try:
            connection=pyodbc.connect(constring)
            mycursor=connection.cursor()
            result = myFunc(mycursor,*args)
            connection.commit()
            connection.close()
            return result
        except Exception as e:
            print('Connection error')
            print(e)
    return innerWrapper

@database_connection
def allGenderList(mycursor):#gets values from Gender table to display
    mycursor.execute('SELECT * FROM Gender')
    gen=mycursor.fetchall()
    return gen

@database_connection
def allBloodGroupList(mycursor):#displays values from BloodGroup table
    mycursor.execute('SELECT * FROM BloodGroup')
    group=mycursor.fetchall()
    return group

@database_connection
def allPatientRecords(mycursor):#gets values from Patient table to display
    mycursor.execute('SELECT * FROM Patient')
    patient=mycursor.fetchall()
    return patient

@database_connection
def listRecords(mycursor,p_id):
    while(True):
        try:
            mycursor.execute('''SELECT patient_id,patient_name,gender,age,blood_group FROM Patient
            JOIN Gender ON Patient.gender_no= Gender.gender_no
            JOIN BloodGroup ON Patient.blood_group_no=BloodGroup.blood_group_no
            WHERE patient_id=?''',(p_id))
            #patient=mycursor.fetchall()
            #print(patient)
            #status=True
        except Exception as e:
                print("Could not search from database")
                print(e)
        else:
            patient=mycursor.fetchall()
            if len(patient)>0:
                for patient_id,patient_name,gender_no,age,blood_group_no in patient:
                    print(f"Patient id: {patient_id}\nPatient name: {patient_name}\nGender: {gender_no}\nAge: {age}\nBlood group: {blood_group_no}")
            else:
                print('This number does not exist in database')
        break
        
def addPatientRec():
    print("Enter the patient details")
    pat_name=input("Enter the patient name:")
    gen=allGenderList()
    for genno,genname in gen:
        print(genno,genname)
    gen_name=int(input("Enter the appropriate number of the patients gender:"))
    Age=int(input("Enter the patient age:"))
    group=allBloodGroupList()
    for grpno,grp in group:
        print(grpno,grp)
    Group=int(input("Enter the appropriate number of the patients blood group:"))
        
    while(True):
        try:
            connection = pyodbc.connect(constring)
            mycursor = connection.cursor()
            try:
                mycursor.execute("INSERT INTO Patient(patient_name,gender_no,age,blood_group_no) VALUES (?,?,?,?)",(pat_name,gen_name,Age,Group))           
            except Exception as e:
                print("Could not write to database")
                print(e)
            else:
                print("Record addition successful")
            break
        except:
            print("Record addition unsuccessful")
            continue
    connection.commit()
    connection.close()


def updatePatientRec():
    op1=1
    id=int(input("Enter the patient id of the patient to be updated:"))
    print('''
    1. Update patient name
    2. Update patient gender
    3. Update patient age
    4. Update patient blood group
    ''')
    while(op1==1):
        updateop=int(input("Enter the field to be updated:"))
        connection = pyodbc.connect(constring)
        mycursor = connection.cursor()
        if updateop==1:
            pat_name=input("Enter the new patient name:")
            mycursor.execute("UPDATE Patient SET patient_name=? WHERE patient_id=?",(pat_name,id))
        elif updateop==2:
            gen=allGenderList()
            for genno,genname in gen:
                print(genno,genname)
            gen_name=int(input("Enter the appropriate number of the patients gender:"))
            mycursor.execute("UPDATE Patient SET gender_no=? WHERE patient_id=?",(gen_name,id))
        elif updateop==3:
            Age=input("Enter the new patient age:")
            mycursor.execute("UPDATE Patient SET age=? WHERE patient_id=?",(Age,id))
        elif updateop==4:
            group=allBloodGroupList()
            for grpno,grp in group:
                print(grpno,grp)
            Group=int(input("Enter the appropriate number of the patients blood group:"))
            mycursor.execute("UPDATE Patient SET blood_group_no=? WHERE patient_id=?",(Group,id))
        else:
            print("Invalid option")
            break
        op1=int(input("Do you want to update again?(1/0):"))
    connection.commit()
    connection.close()

def deletePatientRec():
    p_id=int(input("Enter the patient id of the record to be deleted:"))
    while(True):
        try:
            connection = pyodbc.connect(constring)
            mycursor = connection.cursor()
            try:
                mycursor.execute("DELETE FROM Patient WHERE patient_id=?",(p_id))           
            except Exception as e:
                print("Could not delete from database")
                print(e)
            else:
                if mycursor.rowcount>0:
                    print("Contact deleted successfully")
                else:
                    print('This record does not exist in database')
            break
        except:
            print("Record deletion unsuccessful")
            continue
    connection.commit()
    connection.close()

def searchPatientRec():
    status=False
    p_id=int(input("Enter the patient id of the record to be searched:"))
    listRecords(p_id)
    

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