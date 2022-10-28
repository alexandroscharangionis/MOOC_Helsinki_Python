def print_sudoku(sudoku: list):
    print()
    print()
    # for row in sudoku:
    for i in range(1, 10):
        count = 1
        # for col in row:
        for col in sudoku[i - 1]:
            if count % 3 == 0:
                print("_  ", end="") if col == 0 else print(f"{col}  ", end="")
            else:
                print("_ ", end="") if col == 0 else print(f"{col} ", end="")
            count += 1
        if i % 3 == 0:
            print()
            print()
        else:
            print()


def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number
