# Write a program that takes an array A and an index i into A, and rearranges the elements such
# that all elements less than A[i] (the "pivot") appear first, followed by elements equal to the pivot,
# followed by elements greater than the pivot.


def partition(A, i):
    pivot = A[i]
    less_pos = 0
    greater_pos = len(A) - 1

    for s in range(len(A)):
        if A[s] < pivot:
            A[s], A[less_pos] = A[less_pos], A[s]
            less_pos += 1

    for l in reversed(range(len(A))):
        if A[l] < pivot:
            break
        if A[l] > pivot:
            A[l], A[greater_pos] = A[greater_pos], A[l]
            greater_pos -= 1





if __name__ == '__main__':
    A = [11, 0, 1, 5, 2, 0, 2, 1, 21, 2]
    print('Before : ', A)
    partition(A, 4)
    print('After partition : ', A)
