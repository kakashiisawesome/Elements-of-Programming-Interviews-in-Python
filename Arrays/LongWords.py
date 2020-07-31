

def printLongWords(words):
    res = []
    for w in words:
        if len(w) > 10:
            res.append(w[0]+str(len(w)-2)+w[len(w)-1])
        else:
            res.append(w)

    for i in res:
        print(i)


if __name__ == '__main__':
    numOfWords = int(input())
    words = []
    for i in range(numOfWords):
        words.append(input())
    printLongWords(words)