def sudoku_grid_correct(sudoku: list):
    for row in range(0, 9):
        if not row_correct(sudoku, row):
            return False

    for column in range(0, 9):
        if not column_correct(sudoku, column):
            return False

    for row in range(0, 9, 3):
        for column in range(0, 9, 3):
            if not block_correct(sudoku, row, column):
                return False

    return True


def row_correct(sudoku: list, row_no: int):
    previous = 0
    for number in sorted(sudoku[row_no]):
        if number != 0 and number == previous:
            return False
        previous = number

    return True


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


def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    previous = 0
    for row in sudoku[row_no: row_no + 3]:
        for number in row[column_no: column_no + 3]:
            numbers.append(number)

    for number in sorted(numbers):
        if number != 0 and number == previous:
            return False
        previous = number
    return True
