list = []

while True:
    user_input = input("Word: ")

    if user_input in list:
        print(f"You typed in {len(list)} different words")
        break
    list.append(user_input)