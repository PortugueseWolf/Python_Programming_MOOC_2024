def read_input(command: str, lower: int, upper: int) -> int:
    while True:
        try:
            input_number = input("Please type in an number: ")
            number = int(input_number)

            if number >= lower and number <= upper:
                return number
            
        except ValueError:
            pass
        
        print(f"You must type in an integer between {lower} and {upper}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)  