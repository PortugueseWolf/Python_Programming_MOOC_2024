def most_common_character(string: str) -> chr:
    all_seen = ""
    character = ""
    count = 0

    for i in string:
        if string.count(i) > count and i not in all_seen:
            character = i
            all_seen += i
            count = string.count(i)
    
    return character

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))