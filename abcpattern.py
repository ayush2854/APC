n = int(input("Enter a number:"))
a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for i in range(0,n):
    for j in range(0,i+1):
        print(a[j],end=" ")
    print()