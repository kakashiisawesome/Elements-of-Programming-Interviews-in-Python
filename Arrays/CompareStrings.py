

def numSmallerByFrequency(queries, words):
    answer = []
    fq = []
    fw = []

    for q in queries:
        fq.append(f(q))

    for w in words:
        fw.append(f(w))

    fw.sort()
    memo = {}
    for i in fq:
        j = 0
        if i not in memo:
            while j < len(fw) and fw[j] <= i:
                j += 1
            memo[i] = len(fw) - j

        answer.append(memo[i])



    # for q in queries:
    #     num = 0
    #     fq = f(q)
    #     for w in words:
    #         if f(w) > fq:
    #             num += 1
    #     answer.append(num)

    return answer


def f(s):
    a = sorted(s)
    count = 0
    i = 0
    while i < len(a) and a[i] == a[0]:
        count += 1
        i += 1

    return count

q = ["aabbabbb","abbbabaa","aabbbabaa","aabba","abb","a","ba","aa","ba","baabbbaaaa","babaa","bbbbabaa"]
w = ["b","aaaba","aaaabba","aa","aabaabab","aabbaaabbb","ababb","bbb","aabbbabb","aab","bbaaababba","baaaaa"]
print(numSmallerByFrequency(q, w))


