limit = int(input("Limit: "))
start = 1
sum = 0
text = "The consecutive sum: 1"

while sum < limit:
    sum += start
    
    if sum >= limit:
        print(f"{text}  = {sum}")
    
    start += 1
    text += f" + {start}"