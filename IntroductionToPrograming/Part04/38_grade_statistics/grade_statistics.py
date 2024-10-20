def user_input() -> list:
    return_list = []

    while True:
        student_grades = []
        user = input("Exam points and exercises completed: ")
        
        if user == "":
            return return_list
        
        splitter = user.split(" ")
        student_grades.append(int(splitter[0]))
        exercise = int(splitter[1]) // 10
        student_grades.append(exercise)
        return_list.append(student_grades)

def point_average(list: list) -> float:
    sum = 0
    count = 0

    for i in list:
        sum += i[0] + i[1]
        count +=2

    return sum / (count / 2)

def grade_processor(list: list) -> list:
    grades = []

    for i in list:
        if i[0] < 10:
            grades.append(0)
            continue
        total_points = i[0] + i[1]

        if total_points < 15:
            grades.append(0)
        if total_points > 14 and total_points < 18:
            grades.append(1)
        if total_points > 17 and total_points < 21:
            grades.append(2)
        if total_points > 20 and total_points < 24:
            grades.append(3)
        if total_points > 23 and total_points < 28:
            grades.append(4)
        if total_points > 27:
            grades.append(5)

    return grades

def statistics(list: list, average: float) -> None:
    print("Statistics:")
    print(f"Points average: {average}")
    pass_percentage = 100 - (list.count(0)/len(list)) * 100
    print(f"Pass percentage: {pass_percentage:.1f}")
    
    print("Grade distribution:")

    i = 5

    while i >= 0:
        star = "*"
        print(f"{i}: {star * list.count(i)}")
        i -= 1

inputs = user_input()
averages = point_average(inputs)
grades = grade_processor(inputs)
statistics(grades, averages)
