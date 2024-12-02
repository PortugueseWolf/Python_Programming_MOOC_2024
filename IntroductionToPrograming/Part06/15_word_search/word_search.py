def find_words(search_term: str) -> list:
    words_found = []
    dot_index = search_term.find(".")
    star_index = search_term.find("*")


    with open("words.txt", "r") as dictionary:
        for line in dictionary:
            line = line.strip()

            if "." in search_term:
                if len(line) == len(search_term) and line[:dot_index] == search_term[:dot_index] and line[dot_index+1:] == search_term[dot_index+1:]:
                    words_found.append(line)

            if "*" in search_term:
            
    print(words_found)
    
    return words_found

if __name__ == "__main__":
    print(find_words("p.ng"))