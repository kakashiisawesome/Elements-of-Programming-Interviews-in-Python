

def customSortString(S, T):
    map = {}
    res = []

    for c in T:
        if c in map:
            map[c] += 1
        else:
            map[c] = 1

    for c in S:
        if c in map:
            times = map.pop(c)
            for i in range(times):
                res.append(c)

    for k in map:
        times = map[k]
        for i in range(times):
            res.append(k)

    return ''.join(res)



customSortString('cbadhs', 'acdbshytbadcdabcsa')