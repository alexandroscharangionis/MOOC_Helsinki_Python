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
