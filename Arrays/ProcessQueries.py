
def processQueries(queries, m):
    arr = [i for i in range(1, m+1)]
    res = []
    for q in queries:
        i = popToFront(arr, q)
        res.append(i)

    return res




def popToFront(arr, k):
    index = -1
    for i in range(len(arr)):
        if arr[i] == k:
            index = i
            break

    for i in range(index-1, -1, -1):
        arr[i+1] = arr[i]

    arr[0] = k
    return index


print(processQueries([3,1,2,1], 5))
