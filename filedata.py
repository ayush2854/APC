# first file write mode  
# second file append mode 
# add data from file one to our third file
# append data from file one to our third file 
# take pointer to zero in third file
# Read first 10 characters
# read(10)
# check the pointer location 

with open("fileone.txt","r") as f1:
    data = f1.read()

with open("filethree.txt","w") as f3:
    f3.write(data)
    f3.write("\n")

with open("filetwo.txt","r") as f2:
    datatwo = f2.read()

with open("filethree.txt","a") as f3:
    f3.write(datatwo)

with open("filethree.txt","r") as f3:
    f3.seek(0)
    print(f3.read(10))
    print(f3.tell())
