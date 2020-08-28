


def setZeros(matrix):
    zeroIndices = []
    rows = len(matrix)
    cols = len(matrix[0])
    doneR = [False]*rows
    doneC = [False]*cols

    # Store indices of zeros
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zeroIndices.append([i, j])

    # Iterate over zeroIndices and set surrounding elements 0

    for index in zeroIndices:
        # Vertical
        if not doneC[index[1]]:
            for i in range(rows):
                matrix[i][index[1]] = 0
            doneC[index[1]] = True


        # Horizontal
        if not doneR[index[0]]:
            for i in range(cols):
                matrix[index[0]][i] = 0
            doneR[index[0]] = True




print(setZeros([[1,1,1],[1,0,1],[1,1,1]]))
