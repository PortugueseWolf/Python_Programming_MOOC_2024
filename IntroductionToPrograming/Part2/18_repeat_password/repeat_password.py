password = input("Password: ")

while True:
    repeat = input("Repeat password: ")

    if repeat == password:
        break

    print("They do not match!")

print("User account created!")