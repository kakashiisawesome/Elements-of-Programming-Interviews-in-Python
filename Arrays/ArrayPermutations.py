# Write a program that takes an integer argument and returns all the primes between 1 and that
# integer. For example, if the input is 18, you should return <2,3,5,7,77,13,\7>.

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


