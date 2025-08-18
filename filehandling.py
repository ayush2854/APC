with open ("hello.txt","r+") as file:
    file.writelines("hello")
    file.write(" Welcome to python programming")
    print(file.tell())
    file.seek(6)
    print(file.read())