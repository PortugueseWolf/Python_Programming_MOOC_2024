from random import randint

def generate_strong_password(x: int, has_numbers: bool, has_symbols: bool) -> str:
    characters = ""
    password = ""
    guaranteed_leter = randint(0, x)
    guaranteed_number = randint(0, x)
    guaranteed_symbol = randint(0, x)

    for i in range(97, 123):
        characters += chr(i)

    if has_numbers:
        for i in range(48, 57):
            characters += chr(i)
            

        
    if has_symbols:
        characters += "!?=+-()#"

    for i in range(x):
        password += characters[randint(0,len(characters) - 1)]

    if has_numbers

    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(5, False, True))