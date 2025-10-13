class Animal:
    def sound(self):
        print("Animals make different sounds")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")
  
d = Dog()
d.sound() 