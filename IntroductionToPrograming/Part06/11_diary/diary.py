data = []

with open("diary.txt") as diary:
    for line in diary:
        line = line.strip()
        data.append(line)

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    user_option = int(input("Function: "))

    if user_option == 1:
        entry = input("Diary entry: ")
        data.append(entry)
        
    if user_option == 2:
        print("Entries:")
        for line in data:
            print(line)

    if user_option == 0:
        with open("diary.txt", "w") as diary:
            for entry in data:
                diary.write(f"{entry}\n")
        print("Bye now!")
        break