def no_vowels(string: str) -> str:
    vowels = "aeiou"
    return_string = ""
    
    for i in string:
        if i not in vowels:
            return_string += i
    
    return return_string

if __name__ == "__main__":

    my_string = "this is an example"
    print(no_vowels(my_string))