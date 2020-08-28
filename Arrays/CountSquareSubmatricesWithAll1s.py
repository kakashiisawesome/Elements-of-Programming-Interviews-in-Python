

def checkSubMatrix(x, y, n, matrix):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if matrix[i][j] != 1:
                return False

    return True


def countSquares(matrix):
    m = len(matrix)
    n = len(matrix[0])
    res = 0
    # Count all 1X1 matrices
    for row in matrix:
        for e in row:
            if e == 1:
                res += 1

    # Count all kXk matrices possible, k > 1
    limit = min(m, n)
    for k in range(2, limit+1):
        for i in range(m):
            for j in range(n):
                if i <= m-k and j <= n-k:
                    if checkSubMatrix(i, j, k, matrix):
                        res += 1

    return res


a = [[0,1,1,1], [1,1,1,1], [0,1,1,1]]

print(countSquares(a))