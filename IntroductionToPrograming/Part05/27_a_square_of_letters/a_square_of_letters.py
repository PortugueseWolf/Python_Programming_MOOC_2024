number_to_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

layers = int(input("Layers: "))
# 64
outer_limit = layers * 2 - 1

for index in range(0, outer_limit):
    print(chr(65 + layers) * (outer_limit - index))