class Animal:
    def __init__(self):
        pass 

class Cat(Animal):
    def __init__(self,color,name):
        self.color = color
        self.name = name

    def show(self):
        print("It is a Cat")
        print(f"Color is: {self.color}")
        print(f"Name is: {self.name}")

class Dog(Animal):
    def __init__(self,color,name):
        self.color = color
        self.name = name

    def show(self):
        print("It is a Dog")
        print(f"Color is: {self.color}")
        print(f"Name is: {self.name}")

c = Cat("White","Tom")
c.show()

d = Dog("Black","Rocky")
d.show()

class Pet(Cat,Dog):
    def Details(self):
        print("It is a pet")

p = Pet(Cat,Dog)
p.Details()