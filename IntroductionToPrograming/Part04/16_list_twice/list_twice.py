list = []

while True:
    user_input = int(input("New item: "))

    if user_input == 0:
        print("Bye!")
        break

    list.append(user_input)

    print(f"The list now: {list}")
    print(f"The list in order: {sorted(list)}")