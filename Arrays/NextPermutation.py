# Algorithm:
# 1. Find longest non increasing suffix
# 2. Identify pivot(element before the suffix)
# 3. Find rightmost successor to pivot in suffix and swap pivot with it
# 4. Reverse the suffix


def nextPermutation(nums):
    if len(nums) > 1:
        flag = True
        imax = 0
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                imax = i
                flag = False

        for j in range(imax+1, len(nums)):
            if nums[j] > nums[i]:
                jmax = j

        nums[i], nums[j] = nums[j], nums[i]

        nums[i+1:] = nums[:i:-1]

        if flag:
            nums.sort()



a = [1,2,3,4,5,6]

a[2:] = a[:1:-1]
print(a)