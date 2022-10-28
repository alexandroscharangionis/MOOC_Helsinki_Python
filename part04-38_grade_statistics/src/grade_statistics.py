def main():
    total_students = 0
    grade0 = 0
    grade1 = 0
    grade2 = 0
    grade3 = 0
    grade4 = 0
    grade5 = 0
    total_points = 0

    while True:
        points = input("Exam points and exercises completed: ")
        if points == "":
            break
        else:
            total_students += 1
            exam_points, completed_exercises = points.split(" ")
            exercise_points = get_exercise_points(int(completed_exercises))
            total_points += int(exam_points) + exercise_points

            if int(exam_points) < 10:
                grade0 += 1
            else:
                grade = calculate_grade(int(exam_points), exercise_points)
                match grade:
                    case 0:
                        grade0 += 1
                    case 1:
                        grade1 += 1
                    case 2:
                        grade2 += 1
                    case 3:
                        grade3 += 1
                    case 4:
                        grade4 += 1
                    case 5:
                        grade5 += 1

    pass_percentage = (grade1 + grade2 + grade3 + grade4 +
                       grade5) / total_students * 100
    points_average = total_points / total_students

    print(f"Statistics: ")
    print(f"Points average: {points_average:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")
    print(f"Grade distribution: ")
    for i in range(5, -1, -1):
        print(f"{i}: ", end="")
        if i == 0:
            print("*" * grade0)
        elif i == 1:
            print("*" * grade1)
        elif i == 2:
            print("*" * grade2)
        elif i == 3:
            print("*" * grade3)
        elif i == 4:
            print("*" * grade4)
        else:
            print("*" * grade5)


def get_exercise_points(completed_ex: int):
    if len(str(completed_ex)) == 1:
        return 0
    elif len(str(completed_ex)) == 3:
        return 10
    else:
        return int(str(completed_ex)[0])


def calculate_grade(exam_points, exercise_points):
    total = exam_points + exercise_points
    if 0 <= total <= 14:
        return 0
    elif 15 <= total <= 17:
        return 1
    elif 18 <= total <= 20:
        return 2
    elif 21 <= total <= 23:
        return 3
    elif 24 <= total <= 27:
        return 4
    else:
        return 5


main()
