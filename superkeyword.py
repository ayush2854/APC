# super keyword, class overloading, method overloading, method overriding, abstract

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def show_info(self):
        super().show_info()
        print(f"Student ID: {self.student_id}")

s1 = Student("Ayush", 20, "CSE05")
s1.show_info()


