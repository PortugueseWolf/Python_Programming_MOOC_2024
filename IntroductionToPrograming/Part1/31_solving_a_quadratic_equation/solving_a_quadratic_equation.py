from math import sqrt

a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))

x = (-b + sqrt(b** - 4 * a * c))//2*a
xx = (-b - sqrt(b** - 4 * a * c))//2*a

print()

print(f"The roots are {x} and {xx}")