def row_correct(sudoku: list, row_no: int):
    previous = 0
    for number in sorted(sudoku[row_no]):
        if number != 0 and number == previous:
            return False
        previous = number

    return True
