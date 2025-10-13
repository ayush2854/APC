class Vehicle:
    def Drive(self):
        print("We can drive the vehicle")

class Bike(Vehicle):
    def Wheels(self):
        print("Have two wheels")

class Car(Vehicle):
    def Wheels(self):
        print("Have four wheels")

b = Bike()
b.Wheels()
b.Drive()

c = Car()
c.Wheels()
c.Drive()