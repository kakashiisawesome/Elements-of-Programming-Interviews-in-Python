# No. of ways to climb n stairs
# In such qns start at end- there are two ways to reach last step: from n-1 and n-2
# So we get ways[n] = ways[n-1] + ways[n-2]
# Recurse from n to 1 and fill the trivial case
# The number of ways build itself

def climbStairs(remaining, memo):
    if remaining < 0:
        return 0

    if remaining == 0:
        return 1

    if remaining in memo:
        return memo[remaining]

    memo[remaining] = climbStairs(remaining-1, memo) + climbStairs(remaining-2, memo)

    return memo[remaining]


print(climbStairs(6, {}))