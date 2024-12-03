# dictionary entries plus added while program running
entries = []

# only entries to add to the dictionary so not to comb through the entire dictionary
to_add = []

with open("dictionary.txt", "r") as new_file:
    for line in new_file:
        line = line.strip()
        parts = line.split(";")
        entries.append([parts[0],parts[1]])

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    user_command = int(input("Function: "))

    if user_command == 3:
        with open("dictionary.txt", "a") as new_file:
            for line in entries:
                new_file.write(f"{line[0]};{line[1]}\n")
        print("Bye!")
        break

    if user_command == 1:
        finnish = input("The word in Finnish: ")
        english = input("The word in English: ")

        entries.append([finnish,english])
        to_add.append([finnish,english])

        print("Dictionary entry added")
    
    if user_command == 2:
        search = input("Search term: ")

        for line in entries:
            if search in line[0] or search in line[1]:
                print(f"{line[0]} - {line[1]}")
