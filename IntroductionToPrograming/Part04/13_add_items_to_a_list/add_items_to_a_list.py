list = []
list_size = int(input("How many items: "))
i = 1
while i <= list_size:
    value = int(input(f"Item {i}: "))
    list.append(value)
    i += 1
print(list)
