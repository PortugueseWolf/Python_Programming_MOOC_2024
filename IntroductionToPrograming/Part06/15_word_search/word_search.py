def find_words(search_term: str) -> list:
    words_found = []
    print(search_term[1:])
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

                if search_term.find("*") == 0:
                    if line[(len(search_term)-1):] == search_term[1:]:
                        words_found.append(line)
                else:
                    if line[:len(search_term)-1] == search_term[:len(search_term)-1]:
                        words_found.append(line)
    
    return words_found

if __name__ == "__main__":
    print(find_words("ca*"))