
def minCost(step, cost, memo):
    if step == len(cost)-1:
        memo[step] = cost[step]
        return memo[step]
    if step >= len(cost):
        return 0

    # Try single step
    if step+1 in memo:
        singleCost = memo[step+1]
    else:
        singleCost = minCost(step+1, cost, memo)

    # Try double step
    if step+2 in memo:
        doubleCost = memo[step+2]
    else:
        doubleCost = minCost(step + 2, cost, memo)

    return cost[step] + min(singleCost, doubleCost)


def minCostClimbingStairs(cost):
    memo = {}
    first = minCost(0, cost, memo)
    second = minCost(1, cost, memo)
    return min(first, second)


print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))