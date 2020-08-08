

def majorityElement(nums):
    threshold = len(nums)//2
    nums.sort()
    max = 0
    maxnum = nums[0]
    c = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            c += 1
        else:
            if c > threshold:
                return nums[i-1]
            c = 1

    return nums[len(nums)-1]




print(majorityElement([2,2,1,1,1,2,2]))