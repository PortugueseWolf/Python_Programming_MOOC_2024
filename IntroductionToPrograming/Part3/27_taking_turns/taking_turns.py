n = int(input("Please type in a number: "))
counter = 1

if n % 2 == 0:
    while counter <= n / 2:
        print(counter)
        print(n - counter + 1)
        counter += 1

else:
    while counter <= n / 2 + 1:
        print(counter)
        if counter != n - counter + 1:
            print(n - counter + 1)
        counter += 1