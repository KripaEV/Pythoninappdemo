'''
#exception handling
try:
    div=4//0
    print(div)
except ZeroDivisionError:
    print("dividing by zero not possible")
except:
    print("error")
finally:
    print("will never give up")

#formatting exception msg
try:
    div=4//2
    print(div)
except Exception as e:
    print("dividing no by 0")
    print(f"{type(e).__name__} has occured. More details below:")
    print(e) #prints details of exception
else:#including else; stmt executes if try is successful
    print("division completed and result =",div)
finally:
    print("will never give up")
'''
#nested try-except
try:
    f=open("mynewfile.txt") #opens file
    try:#if file can be created then execute this
        f.write("Ola!")
    except:#if writing cant happen
        print("cant write the file")
    finally:
        f.close()
except:#for file creation 
    print("File cant be opened")


