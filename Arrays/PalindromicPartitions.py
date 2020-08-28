

def isPalindrome(S):
    i, j = 0, len(S)-1
    temp = S.lower()
    while i < j:
        if temp[i] != temp[j]:
            return False
        i += 1
        j -= 1

    return True


# Tries all the partitions and adds palindromic ones to the res list
def palindromicPartitions(s, start, current, res):

    if start == len(s):
        # Append all the current palindromic partitions
        res.append(current)
        return

    # Iterate over the string and partition at each index and check if we get valid partition i.e palindrome
    for end in range(start+1, len(s)+1):
        substring = s[start: end]
        if isPalindrome(substring):
            # Start at next index recursively
            palindromicPartitions(s, end, current+[substring], res)


if __name__ == '__main__':
    s = input('Enter the input string: ')
    partitions = []
    palindromicPartitions(s, 0, [], partitions)

    print('Palindromic partitions are: \n')
    for i in partitions:
        print(i)


# Input: BorrowOrRob
# Output:
# ['B', 'o', 'r', 'r', 'o', 'w', 'O', 'r', 'R', 'o', 'b']
# ['B', 'o', 'r', 'r', 'o', 'w', 'O', 'rR', 'o', 'b']
# ['B', 'o', 'r', 'r', 'o', 'w', 'OrRo', 'b']
# ['B', 'o', 'r', 'r', 'owO', 'r', 'R', 'o', 'b']
# ['B', 'o', 'r', 'r', 'owO', 'rR', 'o', 'b']
# ['B', 'o', 'r', 'rowOr', 'R', 'o', 'b']
# ['B', 'o', 'rr', 'o', 'w', 'O', 'r', 'R', 'o', 'b']
# ['B', 'o', 'rr', 'o', 'w', 'O', 'rR', 'o', 'b']
# ['B', 'o', 'rr', 'o', 'w', 'OrRo', 'b']
# ['B', 'o', 'rr', 'owO', 'r', 'R', 'o', 'b']
# ['B', 'o', 'rr', 'owO', 'rR', 'o', 'b']
# ['B', 'o', 'rrowOrR', 'o', 'b']
# ['B', 'orro', 'w', 'O', 'r', 'R', 'o', 'b']
# ['B', 'orro', 'w', 'O', 'rR', 'o', 'b']
# ['B', 'orro', 'w', 'OrRo', 'b']
# ['B', 'orrowOrRo', 'b']
# ['BorrowOrRob']
