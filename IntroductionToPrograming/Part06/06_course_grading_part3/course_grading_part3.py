if True:
    student_file = input("Student information: ")
    exercise_file = input("Exercises completed: ")
    exam_file = input("Exam points: ")
else:
    student_file = "students1.csv"
    exercise_file = "exercises1.csv"
    exam_file = "exam_points1.csv"

student_data = {}
exercise_number = {}
exercise_points = {}
exam_points = {}
student_grades = {}
 
with open(student_file) as new_file:
    
    for line in new_file:
        cleaner = line.replace("\n", "")
        splitter = cleaner.split(";")
        if splitter[0] == "id":
            continue
        student_data[int(splitter[0])] = splitter[1] + " " + splitter[2]

    
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
        exercise_points[int(splitter[0])] = points
        exercise_number[int(splitter[0])] = sum
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
print(f"{"name":30}{"exec_nbr":<10}{"exec_pts.":<10}{"exm_pts.":<10}{"tot_pts.":10}grade")
for i in student_data.items():
    name = i[1]
    exec_nbr = exercise_number[i[0]]
    exec_pts = exercise_points[i[0]]
    exm_pts = exam_points[i[0]]
    tot_pts = exec_pts + exm_pts
    grade = 0

    if tot_pts < 15:
        grade = 0
    if tot_pts >= 15 and tot_pts <= 17:
        grade = 1
    if tot_pts >= 18 and tot_pts <= 20:
        grade = 2
    if tot_pts >= 21 and tot_pts <= 23:
        grade = 3
    if tot_pts >= 24 and tot_pts <= 77:
        grade = 4
    if tot_pts >= 28:
        grade = 5

    print(f"{name:<30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{tot_pts:<10}{grade:<10}")
