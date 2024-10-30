layers = int(input("Layers: "))
# 64
outer_limit = layers * 2 - 1
square = []


for index in range(0, outer_limit):
    if index == 0:
        line = chr(64 + layers) * outer_limit
        square.append(line)
    
    if index > 0 and index < layers:
        line = 
for line in square:
    print(line)