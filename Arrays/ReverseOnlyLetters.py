

def reverseOnlyLetters(S):
    a = [c for c in S]

    i, j = 0, len(a)-1

    while i < j:
        if not a[i].isalpha() or not a[j].isalpha():
            if not a[j].isalpha():
                j -= 1
            if not a[i].isalpha():
                i += 1
            continue

        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return ''.join(a)


print(reverseOnlyLetters('Test1ng-Leet=code-Q!'))

