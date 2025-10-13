class Vehicle:
    def Drive(self):
        print("We can drive a vehicle")

class Twowheel(Vehicle):
    def Wheels(self):
        print("It have two wheels")

class Bike(Twowheel):
    def Racing(self):
        print("This is a racing bike")

b = Bike()
b.Racing()
b.Wheels()
b.Drive()