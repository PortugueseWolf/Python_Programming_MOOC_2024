user_input = input("Please type in a sentence: ")

while True:
    print(user_input[0:1])
    if " " in user_input:
        index = user_input.find(" ")
        user_input = user_input[index + 1:]
    else:
        break