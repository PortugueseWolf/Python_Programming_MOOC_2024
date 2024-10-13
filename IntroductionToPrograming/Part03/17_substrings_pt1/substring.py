user_input = input("Please type in a string: ")
count = 1
while count <= len(user_input):
    print(user_input[:count])
    count += 1