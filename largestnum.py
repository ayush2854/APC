n = int(input("Enter how many numbers: "))
i = 1
largest = int(input("Enter number 1: "))

while i < n:
    num = int(input("Enter number " + str(i+1) + ":"))
    if num > largest:
        largest = num
    i+= 1

print("The largest number is:", largest)
