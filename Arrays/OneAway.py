
def oneAway(s, t):
    if abs(len(s) - len(t)) > 1:
        return False

    diff = 0
    map  = dict()

    for c in s:
        if c in map:
            map[c] += 1
        else:
            map[c] = 1

    for c in t:
        if c not in map:
            diff += 1
            if diff > 1:
                return False
        else:
            map[c] -= 1


    for i in map.values():
        diff += i

    print('diff = ', diff)

    return diff <= 1



print(oneAway('tale', 'pale'))