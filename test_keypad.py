def time_to_input(code, keypad):
    result = 0
    dic_neighbors = get_dic_neighbors(keypad)

    prev_key = code[0]

    for key in code[1:]:
        if key == prev_key:
            continue

        if key in dic_neighbors[prev_key]:
            result += 1
        else:
            result += 2
        prev_key = key

    return result

def get_matrix_from_string(string):
    return [list(string[x:x+3]) for x in (0, 3, 6)]

def get_dic_neighbors(keypad):
    matrix = get_matrix_from_string(keypad)
    dic = {}
    for row in range(3):
        for col in range(3):
            key = matrix[row][col]
            dic[key] = get_neighbors(row, col, matrix)
    return dic

def get_neighbors(row, col, matrix):
    neighbors = []
    for i in range(row - 1, row + 2):
        if not (0 <= i < 3):
            continue
        for j in range(col - 1, col + 2):
            if 0 <= j < 3 and (i, j) != (row, col):
                neighbors.append(matrix[i][j])
    return neighbors
