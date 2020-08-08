

def smallerThan(nums):
    res = [0]*len(nums)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                if nums[j] < nums[i]:
                    res[i] += 1

    return res



smallerThan([7,7,7,7])