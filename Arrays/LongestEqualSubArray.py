# Write a program that takes an array of integers and finds the length of a longest subarray
# all of whose entries are equal.

def longestSubArray(A):
    longest, curr_longest = 1, 1

    for i in range(1, len(A)):
        if A[i] == A[i-1]:
            curr_longest += 1
        else:
            longest = max(longest, curr_longest)
            curr_longest = 1


    return longest


if __name__ == '__main__':
    print(longestSubArray([1,1,2,2,2,3,0,0,0,0,4,4]))