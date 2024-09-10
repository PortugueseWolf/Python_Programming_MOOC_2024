limit = int(input("Limit: "))
start = 1
sum = 0

while sum < limit:
    sum += start
    if sum >= limit:
        print(sum)
    start += 1