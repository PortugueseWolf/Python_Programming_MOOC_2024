def find_words(search_term: str) -> list:
    words_found = []

    with open("words.txt", "r") as dictionary:
        for line in dictionary:
            line = line.strip()

            if "." in search_term:
                if len(line) == len(search_term):
                    char_counted = 0
                    for i in range(len(search_term)):
                        if search_term[i] == ".":
                            char_counted += 1
                            continue
                        if search_term[i] == line[i]:
                            char_counted += 1
                    
                    if char_counted == len(search_term):
                        words_found.append(line)
            
            if "*" in search_term:
                
    
    return words_found

if __name__ == "__main__":
    print(find_words("p.n."))