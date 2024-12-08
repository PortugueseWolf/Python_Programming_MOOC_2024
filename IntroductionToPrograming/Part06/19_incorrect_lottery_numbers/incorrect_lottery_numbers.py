def filter_incorrect() -> None:
    correct_numbers = []
    good_line = True

    with open("lottery_numbers.csv", "r") as numbers:
        for line in numbers:
            line = line.strip()
            parts = line.split(";")
            week = parts[0].split(" ")
            try:
                week_number = int(week[1])
            except:
                continue

            numbers = parts[1].split(",")

            if len(numbers) != 7:
                continue

            repeat_numbers = []
            for number in numbers:
                try:
                    lottery_number = int(number)
                except:
                    good_line = False
                    break
                
                if lottery_number in repeat_numbers:
                    good_line = False
                    break

                if lottery_number < 1 or lottery_number > 39:
                    good_line = False
                    break

                repeat_numbers.append(lottery_number)

            if good_line:
                correct_numbers.append(line)

            repeat_numbers.clear()
            good_line = True

    try:
        with open("correct_numbers.csv", "w") as new_file:
            for line in correct_numbers:
                new_file.write(line + "\n")
    except:
        print("Error writing to file")

if __name__ == "__main__":
    filter_incorrect()
