with open("modes.txt","r") as file:
    print(file.read())

with open("modes.txt","w") as file:
    file.write("This is the text written with write method")

with open("modes.txt","a") as file:
    file.write("\nThis is the text written with append method")

with open("modes.txt","r+") as file:
    file.write("\nThis is text written with r+ method")

with open("modes.txt","w+") as file:
    file.write("\nThis is the text written with w+ method ")

with open("modes.txt","a+") as file:
    file.write("\nThis is the text written with a+ method")

with open("modes.txt","rb") as file:
    print(file.readlines())
