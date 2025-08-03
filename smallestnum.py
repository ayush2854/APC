n = int(input("Enter how many number:"))
i=1

smallest = int(input("Enter number 1:"))

while i<n:
    num = int(input("Enter number"+ str(i+1) + ":"))
    if num < smallest:
        smallest = num
    i+=1

print("Smallest number is", smallest)