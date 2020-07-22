# Write a program that takes an array A of n numbers, and rearranges A's elements to get a new array
# BhavingthepropertythatB[0] < B[1] >Bl2) < B[3] >8141< B[5] >....

import random


def shuffleArray(A):

    for i in range(len(A)-1):
        if i%2 == 0:
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
        else:
            if A[i] < A[i+1]:
                A[i], A[i + 1] = A[i + 1], A[i]

    print(A)


if __name__ == '__main__':
    A = []
    for i in range(10):
        A.append(random.randint(0, 100))

    shuffleArray(A)
