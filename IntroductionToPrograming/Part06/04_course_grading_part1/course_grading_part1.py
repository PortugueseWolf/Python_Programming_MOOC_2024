

if True:
    student_file = input("Student information: ")
    exercise_file = input("Exercises completed: ")
else:
    # now this is the False branch, and is never executed
    student_file = "students1.csv"
    exercise_file = "exercises1.csv"

student_data = {}
exercise_data = {}
 
with open(student_file) as new_file:
    raw = []
    for line in new_file:
        cleaner = line.replace("\n", "")
        splitter = cleaner.split(";")
        if splitter[0] == "id":
            continue
        raw.append(splitter[1])
        raw.append(splitter[2])
        student_data[int(splitter[0])] = raw[:]
        raw.clear()
    
with open(exercise_file) as new_file:
    raw = []
    for line in new_file:
        cleaner = line.replace("\n", "")
        splitter = cleaner.split(";")
        if splitter[0] == "id":
            continue

        for i in range(len(splitter)):
            if i == 0:
                continue
            raw.append(int(splitter[i]))
        
        exercise_data[int(splitter[0])] = raw[:]
        raw.clear()

for i in student_data.items():
    print(f"{i[1][0]} {i[1][1]} {sum(exercise_data[i[0]])}")
