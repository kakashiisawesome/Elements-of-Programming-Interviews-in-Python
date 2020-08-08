def swap(chars, i, j):
    ch = chars[i]
    chars[i] = chars[j]
    chars[j] = ch


def reverse(chars, start):
    (i, j) = (start, len(chars) - 1)
    while i < j:
        swap(chars, i, j)
        i = i + 1
        j = j - 1


# Function to find lexicographically next permutations of a
# string. It returns true if the string could be rearranged as
# a lexicographically greater permutation else it returns false
def next_permutation(chars):

    # Find largest index i such that chars[i - 1] is less than chars[i]
    i = len(chars) - 1

    while chars[i - 1] >= chars[i]:

        # if i is first index of the string, that means we are already at
        # highest possible permutation i.e. string is sorted in desc order

        i = i - 1
        if i == 0:
            return False

    # if we reach here, [i..n) is sorted in descending order
    # i.e. chars[i-1] < chars[i] >= chars[i+1] >= chars[i+2] >= ... >= chars[n-1]

    # Find highest index j to the right of index i such that chars[j] > chars[i–1]
    j = len(chars) - 1
    while j > i and chars[j] <= chars[i - 1]:
        j = j - 1

    # swap characters at index i-1 with index j
    swap(chars, i - 1, j)

    # reverse [i..n) and return True
    reverse(chars, i)

    return True




# Function to find all lexicographically next permutations of a
# sorted in ascending order
def permutations(str):

    # convert the string into a list and sort it in ascending order
    chars = sorted(list(str))

    while True:

        # print current permutation
        print(''.join(chars), end=' ')

        # find next lexicographically ordered permutation
        if not next_permutation(chars):
            break


if __name__ == '__main__':

    str = "BADC"
    permutations(str)