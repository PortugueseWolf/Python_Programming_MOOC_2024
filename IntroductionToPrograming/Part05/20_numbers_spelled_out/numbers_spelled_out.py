def dict_of_numbers() -> dict:
    dictionary = {}
    single_digits = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",8: "eight", 9: "nine"}
    teens = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 15: "fifteen", 18: "eighteen"}
    tens = {2: "twenty", 3: "thirty", 5: "fifthy"}

    for number in range(1, 30):
        if number < 10:
            dictionary[number] = single_digits[number]
        if number >= 10 and number <= 13 or number == 15 or number == 18:
            dictionary[number] = teens[number]
        if number == 14 or number >= 16 and number < 20 and number != 18:
            digit = int(str(number)[1])
            dictionary[number] = (single_digits[digit] + "teen")
        if number >= 20:
            first_digit = int(str(number)[1])
            second_digit = int(str(number)[1])
            if first_digit in tens:
                dictionary[number] = (tens[first_digit] + )
      

    print(dictionary)

if __name__ == "__main__":
    dict_of_numbers()