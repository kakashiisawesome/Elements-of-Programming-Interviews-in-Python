

def generate(numRows):
    res = []

    for i in range(numRows):
        if i == 0:
            res.append([1])
        elif i == 1:
            res.append([1,1])
        else:
            temp = [1]
            for j in range(len(res[i-1])-1):
                temp.append(res[i-1][j] + res[i-1][j+1])
            temp.append(1)

            res.append(temp)

    return res



print(generate(3))
