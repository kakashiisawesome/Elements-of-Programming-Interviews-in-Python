# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
from functools import cmp_to_key

def doesOverlap(a, b):
    if (a[1] >= b[0] >= a[0]) or (a[1] >= b[1] >= a[0]) or (a[0] <= b[0] <= b[1] <= a[1]) or (b[0] <= a[0] <= a[1] <= b[1]):
        return True

    return False


def merge(intervals):
    res = []
    s = sorted(intervals, key=cmp_to_key(lambda item1, item2: item1[0] - item2[0]))
    curr_interval = s[0]

    for i in range(1, len(s)):

        if curr_interval[1] >= s[i][0]:
            # Merge with curr_interval
            curr_interval[1] = s[i][1]
        else:
            # Add curr_interval to res
            res.append(curr_interval)
            curr_interval = s[i]

    res.append(curr_interval)

    return res

merge([[1,4],[4,5]])