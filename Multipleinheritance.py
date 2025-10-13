class Twowheel:
    def Wheel(self):
        print("Have two wheels")

class Fourwheel:
    def Wheels(self):
        print("Have four wheels")

class Vehicle(Twowheel,Fourwheel):
    def Drive(self):
        print("We can Drive the vehicle")

v = Vehicle()
v.Drive()
v.Wheel()
v.Wheels()