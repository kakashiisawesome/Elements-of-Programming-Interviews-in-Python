
# Write a program that takes an array denoting the daily stock price, and retums the maximum profit
# that could be made by buying and then selling one share of that stock. There is no need to buy if
# no profit is possible.


def stockProfit(A):
    minPrice = A[0]
    maxProfit = 0

    for i in range(1, len(A)):
        if A[i] < minPrice:
            minPrice = A[i]
        else:
            maxProfit = max(maxProfit, A[i] - minPrice)

    return maxProfit


if __name__ == '__main__':
    stockProfit([310, 315, 275, 295, 260, 270, 290, 230, 255, 250])