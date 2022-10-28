def count_matching_elements(my_matrix: list, element: int):
    matches = 0
    for i in range(len(my_matrix)):
        for j in range(len(my_matrix[i])):
            if element == my_matrix[i][j]:
                matches += 1
    return matches
