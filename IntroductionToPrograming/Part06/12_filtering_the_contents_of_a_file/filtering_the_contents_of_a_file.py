def filter_solutions() -> None:
    correct = []
    incorrect = []

    with open("solutions.csv", "r") as new_file:
        for line in new_file:
            line = line.strip()
            splitter = line.split(";")
            tester = eval(splitter[1])
            if tester == int(splitter[2]):
                correct.append(line)
            else:
                incorrect.append(line)
    
    with open("correct.csv", "w") as new_file:
        for line in correct:
            new_file.write(f"{line}\n")
    
    with open("incorrect.csv", "w") as new_file:
        for line in incorrect:
            new_file.write(f"{line}\n")
