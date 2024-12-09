from random import randint, sample

def generate_strong_password(x: int, has_numbers: bool, has_symbols: bool) -> str:
    characters = ""
    password = ""

    for i in range(97, 123):
        characters += chr(i)

    characters += "!?=+-()#"
    
    for i in range(48, 58):
        characters += chr(i)
    
    if not has_numbers and not has_symbols:
        new_password = sample(characters[:26], x)

        for i in new_password:
            password += i
        
        return password

    if has_numbers and has_symbols:
        new_password = sample(characters, x)

        guaranteed_spots = sample(range(0,x - 1), 3)

        new_password[guaranteed_spots[0]] = characters[randint(0, 26)]     
        new_password[guaranteed_spots[1]] = characters[randint(26, 33)]
        new_password[guaranteed_spots[2]] = characters[randint(33, 43)]
        for i in new_password:
            password += str(i)

        return password

    if has_symbols and not has_numbers:
        new_password = sample(characters[:33], x)

        guaranteed_spots = sample(range(0,x - 1), 2)

        new_password[guaranteed_spots[0]] = characters[randint(0, 26)]      
        new_password[guaranteed_spots[1]] = characters[randint(26, 33)]

        for i in new_password:
            password += str(i)

        return password

    characters = characters[:26] + characters[34:]

    new_password = sample(characters, x)

    guaranteed_spots = sample(range(0,x - 1), 2)
    new_password[guaranteed_spots[0]] = characters[randint(0, 26)] 
    new_password[guaranteed_spots[1]] = characters[randint(26, 35)]

    for i in new_password:
        password += str(i)

    return password

if __name__ == "__main__":
    for i in range(1000):
     print(generate_strong_password(6, True, True))