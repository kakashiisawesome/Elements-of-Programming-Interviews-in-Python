import sys

tripleAllowed = True

def jump(arr, i, points, m, path):
    if i >= len(arr):
        return -1

    tp = -1
    global tripleAllowed
    if tripleAllowed:
        tripleAllowed = False
        tp = jump(arr, i+3, points, 3, path)
        tripleAllowed = True

    sj = jump(arr, i+1, points, 1, path)
    dj = jump(arr, i+2, points, 2, path)

    nextjump = max(tp, max(sj, dj))
    if sj > 0:
        if nextjump == sj:
            path.append(i + 1)
            tripleAllowed = True
        elif nextjump == dj:
            path.append(i+2)
            tripleAllowed = True
        else:
            path.append(i+3)
            tripleAllowed = False

    points += m * arr[i] + nextjump if nextjump > 0 else m * arr[i]

    return points

path = []
print(jump([4,2,3], 0, 0, 1, path))
print(path)

