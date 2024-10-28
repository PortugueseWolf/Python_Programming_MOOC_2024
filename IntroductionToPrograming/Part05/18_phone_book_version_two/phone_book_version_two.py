phone_book = {}

while True:
    command = int(input("command (1 search, 2 add, 3 quitt): "))

    if command == 3:
        print("quitting...")
        break

    if command == 1:
        name = input("name: ")
        if name in phone_book:
            for number in phone_book[name]:
                print(number)
        else:
            print("no number")

    if command == 2:
        name = input("name: ")
        number = input("number: ")
        if name not in phone_book:
            phone_book[name] = []
            phone_book[name].append(number)
        else:
            phone_book[name].append(number)
            
        print("ok!")