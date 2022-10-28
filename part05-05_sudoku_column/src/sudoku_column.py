def column_correct(sudoku: list, column_no: int):
    numbers = []
    previous = 0
    for row in sudoku:
        numbers.append(row[column_no])

    for number in sorted(numbers):
        if number != 0 and number == previous:
            return False
        previous = number

    return True
