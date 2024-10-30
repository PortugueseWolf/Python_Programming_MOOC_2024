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
            sum = 0
            for course in student_database[name]:
                print(f" {course[0]} {str(course[1])}")
                sum += course[1]
            print(f" average grade {sum / len(student_database[name])}")

def add_course(student_database: dict, name: str, course: tuple) -> None:
    if name in student_database:
        student_database[name].append(course)


if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    print_student(students, "Peter")