class Vehicle:
    def Drive(self):
        print("We can Drive the vehicle")

class Car(Vehicle):
    def Wheels(self):
        print("Have four wheels")

c = Car()
c.Drive()
c.Wheels()