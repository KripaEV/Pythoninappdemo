from abc import ABC, abstractmethod

class calculate(ABC):
    @abstractmethod
    def calculation(self,num1,num2):
        pass
    
    @property
    def num1(self):
        return self.__num1
    @num1.setter
    def num1(self, number):
         self.__num1 = number
    
    @property
    def num2(self):
        return self.__num2
    @num2.setter
    def num2(self, number):
        self.__num2 = number

class calcsum(calculate):
    def calculation(self,num1,num2):
        print(f"Sum of {num1} and {num2}:",num1+num2)
    
class calcdiff(calculate):
    def calculation(self,num1,num2):
        print(f"Difference is {num1} and {num2}:",num1-num2)

class calcprod(calculate):
    def calculation(self,num1,num2):
        print(f"Product is {num1} and {num2}:",num1*num2)

class calcquo(calculate):
    def calculation(self,num1,num2):
        print(f"Quotient is {num1} and {num2}:",num1/num2)

add = calcsum()
diff = calcdiff()
pro = calcprod()
quo = calcquo()

num1=int(input("Enter the first no:"))
num2=int(input("Enter the second no:"))
add.calculation(num1,num2)
diff.calculation(num1,num2)
pro.calculation(num1,num2)
quo.calculation(num1,num2)

'''
class calculator:
    #num1=0
    #num2=0
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("Two numbers:",self.num1,self.num2)

    def add(self):
        print("Sum:",self.num1+self.num2)

    def multiply(self):
        print("Product:",self.num1*self.num2)

    def divide(self):
        print("Quotient:",self.num1/self.num2)

cal=calculator(6,2)
cal.add()
cal.multiply()
cal.divide()
'''
