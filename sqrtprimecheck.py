import math

num = int(input("Enter a number:"))
sqr = math.sqrt(num)
isprime = True
i = 2

if sqr < 2:
    isprime = False
else:
    for i in range(2, int(math.sqrt(sqr)) + 1):
        if sqr % i == 0:
            isprime = False
            break

if isprime:
    print("Square root of given number is a prime")
else:
    print("Square root of given number is not prime")


