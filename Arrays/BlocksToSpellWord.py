


def assignWords(target, index, words):
    choices = []
    for w in words:
        if target[index] in w:
            choices.append(w)

    if index == len(target)-1:
        return len(choices) > 0

    for c in choices:
        remaining = words.copy()
        remaining.remove(c)
        if assignWords(target, index+1, remaining):
            return True

    return False



def canSpellWord(words, target):
    if len(words) < len(target):
        return False

    return assignWords(target, 0, words)

print(assignWords('binary', 0, ["bi", "n", "a", "r", "y"]))



# def canSpellWord(words, target):
#     if len(words) < len(target):
#         return False
#
#     targetLetterCount = {}
#     wordSContainingLetter = {}
#
#     for c in target:
#         if c in targetLetterCount:
#             targetLetterCount[c] += 1
#         else:
#             targetLetterCount[c] = 1
#
#         if c not in wordSContainingLetter:
#             for w in words:
#                 if c in w:
#                     if c not in wordSContainingLetter:
#                         wordSContainingLetter[c] = {w}
#                     else:
#                         wordSContainingLetter[c].add(w)
#
#
#     for k in wordSContainingLetter:
#         if len(wordSContainingLetter[k]) < targetLetterCount[k]:
#             return False
#
#     commonWords = wordSContainingLetter[target[0]]
#     for c in target:
#         commonWords = commonWords.intersection(wordSContainingLetter[c])
#
#
#
#
#
#
#
#
# canSpellWord(["how", "do", "i", "shot", "web"], 'wowh')

