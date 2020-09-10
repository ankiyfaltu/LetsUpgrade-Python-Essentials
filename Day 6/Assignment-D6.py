# Problem 1
class bank_ac:
    def __init__(self, ownerName, balance):
        self.ownerName = ownerName
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print('Balance in account of ', self.ownerName, ' is ', self.balance)

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print ('Remaining blance in ', self.ownerName, ' account is ', self.balance)
        else:
            print('Insufficient balance in your account. You can only withdraw upto', self.balance)
            print('')


Ankit = bank_ac('Ankit', 0)
Ankit.deposit(10000)
Ankit.withdrawal(2000)
Ankit.deposit(100000)
Ankit.withdrawal(50000)
Ankit.withdrawal(60000)

# Problem 2
from math import pi, sqrt

class cone:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        print("volume of cone is ", self.height*pi*(self.radius**2)/3)

    def surface_area(self):
        print('Surface area of cone is ', pi*self.radius*(self.radius+sqrt((self.height**2)+(self.radius**2))))

coneA = cone(20, 40)
coneA.volume()
coneA.surface_area()
