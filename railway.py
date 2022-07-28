from abc import ABC
import pyodbc
import functools

constring="Driver={SQL Server};Server=DESKTOP-9FVJH8C\SQLEXPRESS;Database=railway_db;Trusted_Connection=yes;"

def database_connection(myFunc):#decorator to establish and disconnect connection
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


no_of_berths=5
waitlist_tickets=2

@database_connection
def allstops(mycursor):#gets all values from Stations table
    mycursor.execute('SELECT * FROM Stations')
    stat=mycursor.fetchall()
    return stat

@database_connection
def trains(mycursor,dest,name):
    mycursor.execute('SELECT * FROM Trains')
    tr=mycursor.fetchall()
    if 

def bookticket():
    print("Enter the passenger details:")
    stat=allstops()
    print('''Start Station: Trivandrum
    Destinations:
    Station id\tStation name''')
    for stat_id,stat_name in stat:
        if stat_id!=0:
            print(stat_id,stat_name)
    dest=int(input("Enter the destination station id:"))
    name=input("Enter passenger name:")


