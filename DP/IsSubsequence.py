
def isSubsequence(s, t):

    idx = -1
    i = 0
    while i < len(s):
        if idx >= len(t)-1:
            if i <= len(s) - 1:
                return False
            return True
        for j in range(idx+1, len(t)):
            if s[i] != t[j]:
                if j == len(t)-1:
                    return False
            else:
                idx = j
                break
        i += 1

    return i == len(s)


print(isSubsequence('acb', 'ahbgdc'))
