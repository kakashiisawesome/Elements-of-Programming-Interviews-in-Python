
def search(A, t):
    l, r = 0, len(A) - 1

    while l < r:
        m = (l + r) // 2

        if A[m] == t:
            return m

        if A[l] <= A[m]:
            if A[l] <= t <= A[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            if A[m] <= t <= A[r]:
                l = m + 1
            else:
                r = m - 1

    if A[l] == t:
        return l
    else:
        return -1


print(search([3,1], 1))