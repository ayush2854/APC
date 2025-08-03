n = int(input("Enter a number: "))

if n <= 1:
    print("Given number is not prime")
else:
    isprime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            isprime = False
            break
        i += 1

    if isprime:
        print("Given number is a prime")
    else:
        print("Given number is not prime")
