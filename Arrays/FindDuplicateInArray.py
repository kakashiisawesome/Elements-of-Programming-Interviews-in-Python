

def findDuplicate(nums):
    slow, fast = nums[0], nums[0]

    slow = nums[slow]
    fast = nums[nums[fast]]

    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    fast = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


findDuplicate([1,3,4,2,5,2])

#  1 -> 3 -> 2 -> 4 -> 5 --
#            |------------|
