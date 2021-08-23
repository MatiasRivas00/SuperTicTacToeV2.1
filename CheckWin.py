
def check_win(board):

    matrix = board
    matrix.append(matrix[0])
    matrix.append(matrix[1])
    matrix.append(matrix[2])
    for i in matrix:
        if i[0] == i[1] and i[0] == i[2] and i[0] == i[3] and i[0] != " ":
            return True, i[0]
    for j in range(7):
        if matrix[j][0] == matrix[j + 1][1] and matrix[j][0] == matrix[j + 2][2] and matrix[j][0] == matrix[j + 3][3]\
                and matrix[j][0] != ' ':
            return True, matrix[j][0]
    for j in range(7):
        if matrix[j][3] == matrix[j + 1][2] and matrix[j][3] == matrix[j + 2][1] and matrix[j][3] == matrix[j + 3][0] \
                and matrix[j][3] != ' ':
            return True, matrix[j][3]
    for k in range(4):
        Cycle = ""
        for i in range(11):
            Cycle += matrix[i][k]

        if Cycle.find("XXXX") != -1:
            return True, "X"
        elif Cycle.find("OOOO") != -1:
            return True, "O"

    return False, ""
