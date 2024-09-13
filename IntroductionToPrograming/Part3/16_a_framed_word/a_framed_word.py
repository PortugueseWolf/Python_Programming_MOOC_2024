user_input = input("Word: ")
spaces = (28 - len(user_input)) //2
middle = ""

if len(user_input)%2 == 0:
    middle = "*" + " " * spaces + user_input + " " * spaces + "*"
else:
    middle = "*" + " " * spaces + user_input + " " * spaces + " *"

print("*" *30)
print(middle)
print("*" *30)