n = int(input("Please type in a number: "))

x = 1
y = 1

while x <= n:
    while y <= n: 
        print(f"{x} x {y} = {x * y}")
        y += 1
    x += 1
    y = 1
