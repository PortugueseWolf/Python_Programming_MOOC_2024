def filter_incorrect() -> list:
    correct_numbers = []

    with open("lottery_numbers.csv", "r") as numbers:
        for line in numbers:
            line = line.strip()
            parts = line.split(";")
            week = parts[0].split(" ")
            try:
                week_number = int(week[1])
            except:
                continue

            numbers = line[1].split(",")

            try:
                repeat_numbers = []
                for number in numbers:
                    try:
                        lottery_number = int(number)
                    except:
                        
                    
                    if number in repeat_numbers:
                        break

                    if number < 1 or number > 39:
                        break

                    repeat_numbers.append(number)

                    if number in repeat_numbers:
                        break
    
    return correct_numbers

if __name__ == "__main__":
    print(filter_incorrect())
