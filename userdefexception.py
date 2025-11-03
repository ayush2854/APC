class UnderAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise UnderAgeError("You must be at least 18 years old to register.")
    print("Registration successful!")
except UnderAgeError as e:
    print("Custom Error:", e)
