user_input = int(input("Please type in a positive integer: "))

for i in range(-(user_input), user_input + 1):
    if i != 0:
        print(i)