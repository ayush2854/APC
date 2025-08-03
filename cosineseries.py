import math

x = float(input("Enter the value of x (in degrees): "))
n = int(input("Enter number of terms: "))

x = math.radians(x)

cos_x = 0
sign = 1  

for i in range(n):
    term_power = 2 * i
    term_fact = math.factorial(term_power)
    term = sign * (x ** term_power) / term_fact
    cos_x += term
    sign *= -1 

print("Approximate value of cos(x) is:", cos_x)
