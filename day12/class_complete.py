# Program to explain classes and objects

# basic class and object
class student:
    name= "Krishna Teja"
    rollnumber = 29

    def printFullName(self):
        print(self.name)

    def printRollNumber(self):
        print(self.rollnumber)

teja = student()
teja.printFullName()
teja.name = "Sri Krishna"
teja.printFullName()
teja.printRollNumber()

# Create class with constructor
class person:
    name = ''
    rollnumber = ''
    def __init__(self,name,rollnumber):
        self.name = name
        self.rollnumber = rollnumber

    def printFullName(self):
        print(self.name)

    def printRollNumber(self):
        print(self.rollnumber)

teja = person("Krishna Teja",1001)
teja.printFullName()

kumar = person("Rajesh Kumar",1001)
kumar.printFullName()

# Inheritance
class gamers(student):
    power='Shooting'
    game_name = 'Something'

    def gamePlayed(self):
        print(self.game_name)

g = gamers()
g.printFullName()
g.gamePlayed()
