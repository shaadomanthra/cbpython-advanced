from db import *

class Calculator:

    def start(self):
        welcome_msg ='''Welcome to Calculator App. Choose one operation
        1. Addition
        2. Subtraction
        3. Multiplication
        '''
        print(welcome_msg)
        choice = int(input("Enter your choice: "))

        if(choice<1 or choice>3):
            print("Kindly Enter only the given options")
            choice = int(input("Enter your choice: "))

        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        if choice == 1:
            result = self.addition(num1,num2)
        elif choice == 2:
            result = self.subtraction(num1,num2)
        elif choice == 3:
            result = self.multiplication(num1,num2)
        else:
            print("The choice given is not valid")

        print("The result is :",result)


    def addition(self,num1,num2):
        return num1+num2

    def subtraction(self,num1,num2):
        return num1-num2

    def multiplication(self,num1,num2):
        return num1*num2

    # def storeOperation(self,num1,num2,result):
    #     conn = connect('calc.db')

c = Calculator()
c.start()