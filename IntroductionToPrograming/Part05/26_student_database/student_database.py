def add_student(student_database: dict, name: str) -> dict:
    student_database[name] = []

def print_student(student_database: dict, name: str) -> None:
    if name not in student_database:
        print(name + ": no such person in the database")
    else:
        if len(student_database[name]) == 0:
            print(name + ":")
            print(" no completed courses")
        else:
            print(name + ":")
            print(f" {len(student_database[name])} completed courses:")
            sum = 0
            for course in student_database[name]:
                print(f"  {course[0]} {str(course[1])}")
                sum += course[1]
            print(f" average grade {sum / len(student_database[name])}")

def add_course(student_database: dict, name: str, new_course: tuple) -> None:
    
    if name in student_database and new_course[1] > 0:
        for course in student_database[name]:
            if new_course[0] == course[0]:

                if new_course[1] > course[1]:
                    student_database[name].remove(course)
                    student_database[name].append(new_course)
                    return None
                else:
                    return None

        student_database[name].append(new_course)

def summary(student_database: dict) -> None:
    print(f"students {len(student_database)}")

    most = 0
    name_courses = ""
    avg = 0
    name_avg = ""
    for student, courses in student_database.items():
        if len(courses) > most:
            most = len(courses)
            name_courses = student
        sum = 0
        for grade in courses:
            sum += grade[1]
        if sum / len(courses) > avg:
            avg = sum / len(courses)
            name_avg = student
    print(f"most courses completed {most} {name_courses}")
    print(f"best average grade {avg} {name_avg}")


if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 5))
    print_student(students, "Peter")