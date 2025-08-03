n = int(input("Enter number of terms:"))

first = 0
second =1
count=0
 
while count < n:
    print(first, end=" ")
    third = first + second
    first = second
    second = third
    count += 1
    
