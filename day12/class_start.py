# Program to explain classes and objects

# basic class and object
class student:
    name = 'Krishna Teja'
    rollnumber = 2367

    def printFullName(self):
        print(self.name)

    def printRollNumber(self):
        print(self.rollnumber)

s1 = student()
s1.printFullName()

print(s1.name)
s1.name = "Ramesh"
s1.printFullName()

# Create class with constructor
class person:
    name=''
    contact=''
    age=''

    def __init__(self,name,contact,age):
        self.name = name
        self.contact = contact
        self.age = age

    def printData(self):
        print(self.name,self.contact,self.age)

teja = person("Krishna Teja","Hyderabad",25)
raja = person("Rajesh Kumar","Warngal",30)
suresh = person("S Kumar","Chennai",40)

print(teja.name)
print(raja.name)
print(suresh.age)

# Inheritance
class gamers(student):
    power = "Shooting"
    game_name = "Racing"

    def printGame(self):
        print(self.game_name)

g = gamers()
g.printRollNumber()
print(g.power)
