def read_fruits() -> dict:
    dictionary = {}

    with open("fruits.csv") as new_file:
        for line in new_file:
            fruit_data = line.replace("\n", "")
            parts = fruit_data.split(";")
            dictionary[parts[0]] = float(parts[1])
    
    return dictionary

if __name__ == "__main__":
    print(read_fruits())
