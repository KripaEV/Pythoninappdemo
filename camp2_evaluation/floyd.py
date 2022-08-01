'''Q4. The following is called Floyds triangle:
1
2 3
4 5 6
7 8 9 10
11
· · ·
12 13 14 15
Given a positive integer N, write a program that prints N rows of Floyds
triangle, with the rows properly aligned'''

def floydstriangle(N):
    num=0
    for i in range (1,N+1):#no of rows
        #print("row:",i)
        for j in range (1,i+1):
            num+=1
            print(num,end=" ")
        print()

N=int(input("Enter the number of rows:"))
floydstriangle(N)


