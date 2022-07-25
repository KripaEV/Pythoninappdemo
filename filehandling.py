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


