def stocks(prices):
    profit = 0
    smallest = prices[0]
    highest = 0
    for x in range(len(prices)):
        if prices[x] > highest:
            highest = prices[x]
        if prices[x] < highest:
            profit += highest - smallest
            highest = prices[x]
            smallest = prices[x]
    profit += highest - smallest
    return profit

print(stocks([9, 8, 7, 1, 5, 3, 6, 4, 0, 1, 5]))
