class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"The animal's name is {self.name}"

my_animal = Animal("Lion")

print(my_animal.speak())
