number_to_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

layers = int(input("Layers: "))

outer_limit = layers * 2 - 1
line = number_to_letters[layers-1]* outer_limit
print(line)

for index in range(1, outer_limit):
    for char in range(1, outer_limit):
        