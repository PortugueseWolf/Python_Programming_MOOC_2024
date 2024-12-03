def filter_incorrect() -> None:
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

            repeat_numbers = []
            for number in numbers:
                try:
                    lottery_number = int(number)
                except:
                    break
                
                if number in repeat_numbers:
                    break

                if number < 1 or number > 39:
                    break

                repeat_numbers.append(number)
                
            
            if len(numbers) == 7:
