
def minStartValue(nums):

    s = 1
    if nums[0] < 0:
        s = 1 - nums[0]

    last = 0

    while last < len(nums) - 1:
        sum = s
        for i in range(len(nums)):
            sum += nums[i]
            if sum < 1:
                s += abs(sum) + 1
                last = i - 1
                break
            last = i

    return s


print(minStartValue([1,-2,-3]))