students = []
grades = []

def add_student(name, grade):
    students.append(name)
    grades.append(grade)
    print(f"{name} added with grade {grade}.")

def update_grade(name, new_grade):
    if name in students:
        index = students.index(name)
        grades[index] = new_grade
        print(f"Grade updated for {name} to {new_grade}.")
    else:
        print(f"Student {name} not found.")

def remove_student(name):
    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
        print(f"{name} removed from the list.")
    else:
        print(f"Student {name} not found.")

def average_grade():
    if grades:
        avg = sum(grades) / len(grades)
        print(f"Average grade: {avg:.2f}")
    else:
        print("No grades available.")

def highest_lowest():
    if grades:
        highest = max(grades)
        lowest = min(grades)
        print(f"Highest grade: {highest}")
        print(f"Lowest grade: {lowest}")
    else:
        print("No grades available.")

while True:
    print("\n--- Student Grade Management System ---")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Remove Student")
    print("4. Show Average Grade")
    print("5. Show Highest and Lowest Grade")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = float(input("Enter grade: "))
        add_student(name, grade)

    elif choice == "2":
        name = input("Enter student name: ")
        new_grade = float(input("Enter new grade: "))
        update_grade(name, new_grade)

    elif choice == "3":
        name = input("Enter student name: ")
        remove_student(name)

    elif choice == "4":
        average_grade()

    elif choice == "5":
        highest_lowest()

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")