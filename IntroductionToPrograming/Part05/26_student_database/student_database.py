def add_student(student_dictionary: dict, name: str) -> dict:
    student_dictionary[name] = "0"

def print_student(student_dictionary: dict, name: str) -> None:
    if name not in student_dictionary:
        print(name + ": no such person in the database")
    else:
        print(name + ":")
        print(" no completed courses")

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")