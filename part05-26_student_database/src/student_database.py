def add_student(database: dict, name: str):
    database[name] = []


def print_student(database: dict, name: str):
    if name in database:
        print(f"{name}:")
        if database[name] == []:
            print(" no completed courses")
        else:
            print(f" {len(database[name])} completed courses:")
            grade_total = 0
            for entry in database[name]:
                grade_total += entry[1]
                print(f"  {entry[0]} {entry[1]}")
            print(f" average grade {grade_total / len(database[name])}")
    else:
        print(f"{name}: no such person in the database")


def add_course(database: dict, name: str, course: tuple):
    course_name, course_grade = course
    if len(database[name]) > 0:
        for entry in database[name]:
            if entry[0] == course_name:
                if entry[1] < course_grade:
                    database[name].remove(entry)
                    database[name].append(course)
                return

    if course_grade != 0:
        database[name].append(course)


def summary(database: dict):
    print(f"students {len(database)}")

    best_grade = []
    most_courses = []
    counter = 0
    grade_counter = 0
    for student, courses in database.items():
        if len(courses) > counter:
            most_courses = [student, len(courses)]
            counter = len(courses)
        total_grade = 0
        for _ in range(len(courses)):
            total_grade += courses[_][1]
        if total_grade / len(courses) > grade_counter:
            best_grade = [student, total_grade / len(courses)]
            grade_counter = total_grade / len(courses)
    print(f"most courses completed {most_courses[1]} {most_courses[0]}")
    print(f"best average grade {best_grade[1]} {best_grade[0]}")
