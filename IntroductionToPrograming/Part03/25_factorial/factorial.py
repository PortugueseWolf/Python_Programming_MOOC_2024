while True:
    n = int(input("Please type in a number: "))
    
    if n <= 0:
        print("Thanks and bye!")
        break
    
    fact = 1
    mult = 1
    while mult <= n:
        fact = fact * mult
        mult += 1
    
    print(f"The factorial of the number {n} is {fact}")