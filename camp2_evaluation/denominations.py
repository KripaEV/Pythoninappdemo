'''Q3. The denominations in Indian currency are:
|1, |2, |5, |10, |,20, |50, |100, |200, |500, |2000.
Given an amount N, print how many coins/notes make up N'''

deno={2000:0, 500:0, 200:0, 100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}

def denomination(amount):
    while (amount!=0):
        if (amount>=2000):
            amount=amount-2000
            deno[2000]+=1
            #print(amount)
        elif (amount>=500):
            amount=amount-500
            deno[500]+=1
            #print(amount)
        elif (amount>=200):
            amount=amount-200
            deno[200]+=1
            #print(amount)
        elif (amount>=100):
            amount=amount-100
            deno[100]+=1
            #print(amount)
        elif (amount>=50):
            amount=amount-50
            deno[50]+=1
            #print(amount)
        elif (amount>=20):
            amount=amount-20
            deno[20]+=1
            #print(amount)
        elif (amount>=10):
            amount=amount-10
            deno[10]+=1
            #print(amount)
        elif (amount>=5):
            amount=amount-5
            deno[5]+=1
            #print(amount)
        elif (amount>=2):
            amount=amount-2
            deno[2]+=1
            #print(amount)
        elif (amount>=1):
            amount=amount-1
            deno[1]+=1
            #print(amount)
        else:
            #print(amount)
            break
    print("The denomination break up:",deno.items())

N=int(input("Enter an amount:"))
denomination(N)

'''
OUTPUT:
Enter an amount:2640
The denomination break up: dict_items([(2000, 1), (500, 1), (200, 0), (100, 1), (50, 0), (20, 2), (10, 0), (5, 0), (2, 0), (1, 0)])

Enter an amount:3781
The denomination break up: dict_items([(2000, 1), (500, 3), (200, 1), (100, 0), (50, 1), (20, 1), (10, 1), (5, 0), (2, 0), (1, 1)])

Enter an amount:4928
The denomination break up: dict_items([(2000, 2), (500, 1), (200, 2), (100, 0), (50, 0), (20, 1), (10, 0), (5, 1), (2, 1), (1, 1)])


'''