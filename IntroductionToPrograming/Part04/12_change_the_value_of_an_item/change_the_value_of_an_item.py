list = [1, 2, 3, 4, 5]

while True:
    user_index = int(input("Index: "))

    if user_index == -1:
        break

    user_value = int(input("New value: "))

    list[user_index] = user_value
    print(list)