user_input = input("Please type in a string: ")
count = len(user_input) - 1

while count >= 0:
    print(user_input[count:])
    count -= 1