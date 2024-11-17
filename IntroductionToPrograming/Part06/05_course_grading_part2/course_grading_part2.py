if True:
    student_file = input("Student information: ")
    exercise_file = input("Exercises completed: ")
    exam_file = input("Exam points: ")
else:
    student_file = "students1.csv"
    exercise_file = "exercises1.csv"
    exam_file = "exam_points1.csv"

student_data = {}
exercise_data = {}
exam_points = {}
student_grades = {}
 
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
    for line in new_file:
        cleaner = line.replace("\n", "")
        splitter = cleaner.split(";")
        if splitter[0] == "id":
            continue

        sum = 0
        for i in range(len(splitter)):
            if i == 0:
                continue
            sum += int(splitter[i])
        
        points = int((sum * 10) / 40)
        exercise_data[int(splitter[0])] = points
        sum = 0

with open(exam_file) as new_file:
    for line in new_file:
        cleaner = line.replace("\n", "")
        splitter = cleaner.split(";")
        if splitter[0] == "id":
            continue

        sum = 0
        for i in range(len(splitter)):
            if i == 0:
                continue
            sum += int(splitter[i])
        
        exam_points[int(splitter[0])] = sum
        sum = 0

for i in student_data.items():
    name = f"{i[1][0]} {i[1][1]}"
    grade = 0
    point_sum = exercise_data[i[0]] + exam_points[i[0]]
    if point_sum < 15:
        grade = 0
    if point_sum >= 15 and point_sum <= 17:
        grade = 1
    if point_sum >= 18 and point_sum <= 20:
        grade = 2
    if point_sum >= 21 and point_sum <= 23:
        grade = 3
    if point_sum >= 24 and point_sum <= 77:
        grade = 4
    if point_sum >= 28:
        grade = 5
    print(name, grade)
