from random import randint

def lottery_numbers(amount: int, lower: int, upper: int) -> list:
    numbers = []

    while True:
        if len(numbers) == amount:
            break
        number = randint(lower, upper)
        if number not in numbers:
            numbers.append(number)

    numbers.sort()

    return numbers