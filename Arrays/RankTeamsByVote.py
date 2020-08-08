
def rankTeams(votes):
    position = []
    res = []
    for i in range(len(votes[0])):
        temp = []
        for vote in votes:
            temp.append(vote[i])
        position.append(temp)

    for i in range(len(position)):
        # Get team with max frequency on each position and append it to res
        freq = {}
        for t in position[i]:
            if t not in freq:
                freq[t] = 1
            else:
                freq[t] += 1

        maxfreqteam = ''
        maxf = 0
        for k, v in freq:
            if v > maxf:
                maxf = v
                maxfreqteam = k
        for k, v in freq:
            if v == maxf and k != maxfreqteam:
                





a = ''
a = 'kahitri'
print(a)