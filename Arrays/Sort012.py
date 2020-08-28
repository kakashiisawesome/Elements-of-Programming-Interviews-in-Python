# Sort array containing only 0, 1 and 2 without any sorting algo

import random

def sortNums(nums):
    print(nums)

    zeroIndex, twoIndex = 0, len(nums)-1

    i = 0

    while i <= twoIndex:
        if nums[i] == 0:
            nums[i], nums[zeroIndex] = nums[zeroIndex], nums[i]
            if nums[i] == 0:
                i += 1
            zeroIndex += 1
        elif nums[i] == 2:
            nums[i], nums[twoIndex] = nums[twoIndex], nums[i]
            twoIndex -= 1
        else:
            i += 1


    print(nums, nums==sorted(nums))



for i in range(100):
    print('Case ', i+1)
    n = [random.randint(0, 2) for i in range(100)]
    sortNums(n)

