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

