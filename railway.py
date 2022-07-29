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
    status=False
    mycursor.execute('SELECT * FROM Trains WHERE end_id>=?',(dest))
    tr=mycursor.fetchall()
    for train_id,_,train_name,berths_filled,_,_,_ in tr:
        if berths_filled< no_of_berths:
            mycursor.execute("INSERT INTO Passenger_details(psgr_name,station_id,train_id) VALUES (?,?,?);",(name,dest,train_id))
            mycursor.execute("UPDATE Trains SET berths_filled=? WHERE train_id=?",(berths_filled+1,train_id))
            status=True
            print(f"{train_name} is booked successfully")
            return status
    return status

@database_connection
def waitlist(mycursor,dest,name):
    status=False
    mycursor.execute("SELECT * FROM Trains WHERE end_id>=?",(dest))
    tr=mycursor.fetchall()
    for trainId,trainName,wait_list in tr:
        if wait_list< waitlist_tickets:
            mycursor.execute("INSERT INTO Waiting_list(psgr_name,station_id,train_id) VALUES (?,?,?);",(name,dest,trainId))
            mycursor.execute("UPDATE Trains SET wait_list_tickets=? WHERE train_id=?",(wait_list+1,trainId))
            status=True
            print("Added to waiting list")
            return status
    return status

@database_connection
def psgrdetails(mycursor):
    mycursor.execute('''SELECT psgr_no,psgr_name,station_name,train_name FROM Passenger_details
    JOIN Stations ON Passenger_details.station_id=Stations.station_id
    JOIN Trains ON Passenger_details.train_id=Trains.train_id
    ORDER BY Passenger_details.train_id''')
    print("Passenger details:-")
    passgr=mycursor.fetchall()
    print("Passenger no Name Destination Train name")
    for psgr_no,name,stat,tr_name in passgr:
        print(f"{psgr_no} {name} {stat} {tr_name}")

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
    if not trains(dest,name):
        op=input("No trains available. Add to waiting list?(y/n):")
        match(op):
            case 'y':
                if not waitlist(dest,name):
                    print("No spot available in waiting list")
            case 'n':
                print("Added to waiting list")

st=1
while(st==1):
    print('''
    1. List all stations
    2. Book a ticket
    3. Show passenger details
    ''')
    op=int(input("Enter the choice:"))
    match(op):
        case 1:
            station=allstops()
            print(station)
        case 2:bookticket()
        case 3:psgrdetails()

    st=int(input("Do you want to enter another choice?(1/0):"))