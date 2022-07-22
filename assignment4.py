"""
#print the birth stone and personality type
monthno=input("Enter your birth month number:")
match(monthno):
    case '1':
        print("January-People born in January are bold and alert\nStone-Garnet")
    case '2':
        print("February-People born in February are lucky and loyal\nStone-Amethyst")
    case '3':
        print("March-People born in March are naughty and genuis\nStone-Aquamarine")
    case '4':
        print("April-People born in April are caring and strong\nStone-Diamond")
    case '5':
        print("May-People born in May are loving and practical\nStone-Emarald")
    case '6':
        print("June-People born in June are romantic and curious\nStone-Alexandrite")
    case '7':
        print("July-People born in July are adventurous and honest\nStone-Ruby")
    case '8':
        print("August-People born in August are active and hardworking\nStone-Peridot")
    case '9':
        print("September-People born in September are sensitive and pretty\nStone-Sapphire")
    case '10':
        print("October-People born in October are stylish and friendly\nStone-Tourmaline")
    case '11':
        print("November-People born in November are nice and creative\nStone-Citrine")
    case '12':
        print("December-People born in December are confident and freedom loving\nStone-Zircon")
    case _:
        print("Invalid month")
"""

#print nos divisible by 5 and multiple of 8 btn 2000 and 2500
for num in range(2000,2501):
    if num%5==0 and num%8==0:
        print(num)


#create multiplication table frm 1 to 10 getting user input
num=input("Enter the number:")
num=int(num)
for i in range(1,11):
    print(num,"*",i,"=",(num * i))

