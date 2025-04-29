if True:
    student_file = input("Student information: ")
    exercise_file = input("Exercises completed: ")
    exam_file = input("Exam points: ")
    course_file = input("Course information: ")
else:
    student_file = "students1.csv"
    exercise_file = "exercises1.csv"
    exam_file = "exam_points1.csv"
    course_file = "course1.txt"

student_data = {}
exercise_number = {}
exercise_points = {}
exam_points = {}
student_grades = {}
course_name_and_credits = ""
 
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

with open(course_file, "r") as new_file:
    for line in new_file:
        if course_name_and_credits == "":
            splitter = line.split(":")
            course_name_and_credits = splitter[1].strip()
        else:
            splitter = line.split(":")
            course_name_and_credits = course_name_and_credits + ", " + splitter[1].strip() + " credits"

with open("results.txt", "w") as new_file:
    new_file.write(f"{course_name_and_credits}\n")
    new_file.write("=" * len(course_name_and_credits) + "\n")
    new_file.write(f"{"name":30}{"exec_nbr":<10}{"exec_pts.":<10}{"exm_pts.":<10}{"tot_pts.":10}grade\n")
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
        student_grades[i[0]] = grade
        new_file.write(f"{name:<30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{tot_pts:<10}{grade:<10}\n")

with open("results.csv", "w") as new_file:
    for student in student_data.items():
        new_file.write(f"{student[0]};{student[1]};{student_grades[student[0]]}\n")