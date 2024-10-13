count = 0

while True:
    count += 1

    pin = int(input("PIN: "))

    if pin == 4321 and count == 1:
        print(f"Correct! It only took you one single attempt!")
        break
    elif pin == 4321:
        print(f"Correct! It took you {count} attempts")
        break
    print("Wrong")