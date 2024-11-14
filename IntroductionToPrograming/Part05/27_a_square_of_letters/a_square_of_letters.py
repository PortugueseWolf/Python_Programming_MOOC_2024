layers = int(input("Layers: "))


size = layers * 2 - 1

for i in range(size):
    row = ""
    for j in range(size):
        layer = min(i, j, size - 1 - i, size - 1 - j)
        letter = chr(65 + layers - 1 - layer)
        row += letter
    print(row)
