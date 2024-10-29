def dict_of_numbers() -> dict:
    dictionary = {}
    single_digits = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",8: "eight", 9: "nine"}
    teens = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 15: "fifteen", 18: "eighteen"}
    tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 8: "eighty"}

    for number in range(0, 100):
        if number < 10:
            dictionary[number] = single_digits[number]
        
        if number in teens:
            dictionary[number] = teens[number]
        
        if number == 14 or number >= 16 and number < 20 and number != 18:
            digit = int(str(number)[1])
            dictionary[number] = (single_digits[digit] + "teen")
        
        if number >= 20:
            first_digit = int(str(number)[0])
            second_digit = int(str(number)[1])
            
            if second_digit == 0 and first_digit in tens:
                dictionary[number] = (tens[first_digit])
            elif second_digit == 0:
                dictionary[number] = (single_digits[first_digit] + "ty")
            
            if second_digit != 0:
                if first_digit in tens:
                    dictionary[number] = tens[first_digit] + "-" + single_digits[second_digit]
                else:
                    dictionary[number] = (single_digits[first_digit] + "ty-" + single_digits[second_digit])
    return dictionary

if __name__ == "__main__":
    dict_of_numbers()