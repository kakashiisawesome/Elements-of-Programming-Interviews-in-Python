

def apply_permutation(perm, A):
    print(perm)
    for i in range(len(A)):

        next = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]
            perm[next] -= len(perm)
            print(perm)
            print(A)
            next = temp




if __name__ == '__main__':
    apply_permutation([2,0,1,3], ['a', 'b', 'c', 'd'])


