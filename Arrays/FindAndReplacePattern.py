

def findAndReplacePattern(words, pattern):
    map = {}
    res = []

    for word in words:
        addw = True
        for i in range(len(pattern)):
            if pattern[i] not in map:
                if word[i] in map.values():
                    addw = False
                    break
                map[pattern[i]] = word[i]
            else:
                if word[i] != map[pattern[i]]:
                    addw = False
                    break
        if addw:
            res.append(word)
        map.clear()

    return res


findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], 'abb')