

def missingNumber(nums):
    n = len(nums)
    requiredSum = (n*(n+1))//2

    for i in nums:
        requiredSum -= i

    return requiredSum


print(missingNumber([9,6,4,2,3,5,7,0,1]))