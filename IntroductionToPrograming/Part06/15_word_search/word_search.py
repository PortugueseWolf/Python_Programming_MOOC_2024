from xml.etree.ElementInclude import include


def find_words(search_term: str) -> list:
    words_found = []

    with open("words.txt", "r") as dictionary:
        for line in dictionary:
            if "." in search_term:
            
            line = line.strip()
            if search_term.lower() in line:
                .include()
    
    return words_found

