from typing import List

def maxProfit(prices: List[int]) -> int:
    max_price = 0
    total = 0
    k = 0

    for i in range(len(prices) - 1):
        if prices[i + 1] - prices[i] > 0:
            total += prices[i + 1] - prices[i]

    return total

arr = [7,1,5,3,6,4]
result = maxProfit(arr)

print(result)