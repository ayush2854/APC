n = int(input("Enter how many numbers:"))
fact=1
sum = 1
for i in range(1,n+1):
    fact*=i
    sum+= 1/fact
print("Sum of series is :",sum)

