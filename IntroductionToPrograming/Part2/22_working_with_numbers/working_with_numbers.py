print("Please type in integer numbers. Type in 0 to finish.")

sum = 0
count = 0
positive = 0
negative = 0

while True:
    number = int(input("Number: "))

    if number == 0:
        print(f"Numbers typed in {count}")
        print(f"The sum of the numbers is {sum}")
        print(f"The mean of the numbers is {(sum * 1.0) / count}")
        print(f"Positive numbers {positive}")
        print(f"Negative numbers {negative}")    
        break
    
    sum += number
    count += 1

    if number > 0:
        positive += 1
    else:
        negative += 1