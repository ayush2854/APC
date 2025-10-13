from abc import ABC, abstractmethod

class Car(ABC):  #abstract class 
    def mileage(self):  # abstract method
        pass
class Tesla(Car):
    def mileage(self):
        print("The mileage is 30 kmph")
class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25 kmph")

t = Tesla()
t.mileage()

s = Suzuki()
s.mileage()