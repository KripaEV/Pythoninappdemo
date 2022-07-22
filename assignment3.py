import re
#1. Sort list in asc order and print first element in list
studentage=[19,14,21,15,20]
studentage.sort()
print(studentage) #[14, 15, 19, 20, 21]

#2. python program to find second largest no in list
max=studentage[0]
print(max)
for i in range (1 , len(studentage)-1) : 
    if studentage[i]>max :
        max=studentage[i]
print(max) #21

#3.python pgm to print odd no and even no separately in a list
listnumbers=[1,2,3,4,5,6,7,8,9,10]
oddno = listnumbers[::2]
evenno = listnumbers[1:10:2]
print("The odd numbers list are: {} and the even number list are {}".format(oddno, evenno))
#The odd numbers list are: [1, 3, 5, 7, 9] and the even number list are [2, 4, 6, 8, 10]


#4.pgm for reversing a list
studentage=[19,14,21,15,20]
for i in range(len(studentage)-1,0,-1):
    print(studentage[i]) 

#5.pgm to print all odd numbers from 1-50
for i in range(1,50):
    if i%2!=0:
        print(i)

#6.pgm to count even and odd no in list
listnumbers=[1,2,3,4,5,6,7,8,9,10]
evencount=0
oddcount=0
for i in range(0,len(listnumbers)):
    if listnumbers[i]%2==0:
        evencount+=1
    else:
        oddcount+=1
print("No of even no:",evencount)
print("No of odd no:",oddcount)
"""
#No of even no: 5
#No of odd no: 5
"""

#7.write python pgm to remove zeroes
addr = "216.08.094.196"
num = re.sub("0", " ", addr)
print("IP address without zeroes is {} ".format(num))

#8. Write a python program that matches a string that has an 'a' followed by anything, ending in 'b'
msg = "I love kebab"
txt =  re.findall(".*a.*b$", msg)
print(txt) #['I love kebab']


#9. Replace all occurrences of 6 with 'six' and 10 with 'ten' for the given string 'They ate 6 apples and 10 banana'.
msg="They ate 6 apples and 10 banana"
print(msg.replace('6', 'six').replace('10', 'ten'))
#They ate six apples and ten banana