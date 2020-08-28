

def numSplits(s):
    res = 0
    left, right = '', ''

    for i in range(1, len(s)):
        left = s[:i]
        right = s[i:]

        ls = set(left)
        rs = set(right)
        if len(ls) == len(rs):
            res += 1

    return res


print(numSplits('acbadbaada'))

