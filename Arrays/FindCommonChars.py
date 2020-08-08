

def common(A):
    min = 200
    index = -1
    res = []
    for i in range(len(A)):
        if len(A[i]) < min:
            min = len(A[i])
            index = i

    for c in A[index]:
        done = True
        for i in range(len(A)):
            if i == index:
                continue
            if c not in A[i]:
                done = False
                break
            A[i] = A[i].replace(c, '', 1)

        if done:
            res.append(c)

    return res


print(common(["cool","lock","cook"]))
