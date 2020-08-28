

# Rotate matrix 90 degrees clockwise
# 1. Transpose matrix
# 2. Reverse each row for clockwise rotation and reverse each column for anticlockwise rotation


def rotateMatrix(matrix):

    # Transpose
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in matrix:
        print(i)

    # Reverse each row
    for row in matrix:
        row.reverse()

    print(matrix)



rotateMatrix([[1,2,3], [4,5,6], [7,8,9]])