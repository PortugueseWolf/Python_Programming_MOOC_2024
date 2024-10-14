list = []

while True:
    print(f"The list is now {list}")
    user_input = input("a(d)d, (r)emove or e(x)it: ")

    if user_input == "x":
        print("Bye!")
        break
    
    if user_input == "d":
        list.append(len(list) + 1)
    
    if user_input == "r" and len(list) > 0:
        list.remove(len(list))