

def twosum(nums, target):
    # Using hashmap
    map = {}

    for i in range(len(nums)):
        a = nums[i]
        # Search for target-a
        b = target - a
        if b in map:
            return [i, map[b]]
        map[a] = i



twosum([3,3], 6)