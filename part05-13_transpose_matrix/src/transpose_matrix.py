def transpose(matrix: list):
    new_matrix = []
    for row in matrix:
        new_row = []
        for square in row:
            new_row.append(square)
        new_matrix.append(new_row)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = new_matrix[j][i]
