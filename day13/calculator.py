from db import *

class Calculator:

    def start(self):
        welcome_msg ='''Welcome to Calculator App. Choose one operation
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Show latest operations
        '''
        print(welcome_msg)
        choice = int(input("Enter your choice: "))

        if(choice<1 or choice>4):
            print("Kindly Enter only the given options")
            choice = int(input("Enter your choice: "))

        if choice == 4:
            self.retrieveLatestOperations()
            exit()

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
            exit()

        # make an entry into database
        self.storeOperation(num1,num2,result)
        print("The result is :",result)


    def addition(self,num1,num2):
        return num1+num2

    def subtraction(self,num1,num2):
        return num1-num2

    def multiplication(self,num1,num2):
        return num1*num2

    def storeOperation(self,num1,num2,result):
        conn = connect('calc.db')
        query = f"INSERT INTO operations (num1,num2,result) VALUES ({num1},{num2},{result})"
        execute(conn,query)

    def retrieveLatestOperations(self):
        conn = connect('calc.db')
        query = "SELECT * FROM operations"
        result = fetchall(conn,query)
        print(result)



c = Calculator()
c.start()