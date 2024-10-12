n = int(input("Please type in a number: "))
counter = 1
while counter <= n:
    if counter + 1 <= n:
        print(counter + 1)
    print(counter)
    counter += 2