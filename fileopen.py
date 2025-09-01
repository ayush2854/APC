file = open ("hello.txt","r")
print(file.read())

file = open ("hello.txt","a")
file.write("\nThis is second line of hello.txt")