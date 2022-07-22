
#1.GST ASSIGNMENT
price=int(input("Enter the price of the item:"))
gst=int(input("Enter the GST rate:"))

def calculation(price,gst):
    GST=gst/100*price
    CGST=GST/2
    SGST=GST/2
    print("Actual price of item:",price)
    print("Price after CGST:",price+CGST)
    print("Price after applying SGST:",price+SGST)
    print("Total price with GST:",price+GST)

calculation(price,gst)

#2.Phone book
phonebookdict={"JKL":34567,"ABC":12345,"DEF":98765}

from collections import OrderedDict 
def sort():
    for i in sorted(phonebookdict):
        print(i,phonebookdict[i])

def add():
    newname=input("Enter the new name:")
    newno=input("Enter the new phone no:")
    newdict={newname:newno}
    phonebookdict.update(newdict)
    print(phonebookdict)

def delete():
    delname=input("Enter the name to be deleted:")
    del phonebookdict[delname]
    print(phonebookdict)

def searchname():
    flag=0
    sname=input("Enter the name to search:")
    for name,no in phonebookdict.items():
        if sname==name:
            print("Name:",sname,"\nPhone no:",phonebookdict.get(sname))
            flag=1
    if(flag!=1):
        print("Record not found")

def searchno():
    flag=0
    sno=int(input("Enter the no to search:"))
    for name,no in phonebookdict.items():
        if sno==no:
            print("Name:",name,"\nPhone no:",sno)
            flag=1 
            break
    if flag!=1:
        print("Record not found")


while(1):
    print('''
    1.List all contacts
    2.Add a new content 
    3.Delete a contact
    4.Search by name
    5.Search by number
    6.Exit''')
    ch=input("Enter your choice:")
    match(ch):
        case '1':
            print(sort())
        case '2':
            print(add())
        case '3':
            print(delete())
        case '4':
            print(searchname())
        case '5':
            print(searchno())
        case '6':
            break


#3.Rock-Paper-Scissors
import random

def game():
    upoint=0
    cpoint=0
    j=1
    for i in range(5,0,-1):
        print("Turn",j)

        print('''
        1-Rock
        2-Paper
        3-Scissors''')
        choice=int(input("Enter your choice:"))
        chcomp=random.randint(1,3)
        print("Computer:",chcomp)
        if(choice==1 and chcomp==2 or choice==2 and chcomp==3 or choice==3 and chcomp==1):
            cpoint+=1
        elif(choice==1 and chcomp==3 or choice==2 and chcomp==1 or choice==3 and chcomp==2):
            upoint+=1
        else:
            continue
        j+=1
    if(cpoint>upoint):
        print("Computer wins by",cpoint,"points")
    else:
        print("Player wins by",upoint,"points")

print("Start the game")
game()
