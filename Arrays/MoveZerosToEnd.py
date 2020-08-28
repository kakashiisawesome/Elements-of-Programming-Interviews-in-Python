
# Logic is to iterate over the array and move the non-zero elements to the front,
# all the zeros will be left at the end automatically


def moveZerosToEnd(A):
    writeIndex = 0
    print(A)

    for i in range(len(A)):
        if A[i] != 0:
            A[i], A[writeIndex] = A[writeIndex], A[i]
            writeIndex += 1

    print(A)


moveZerosToEnd([1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9])


