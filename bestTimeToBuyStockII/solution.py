from typing import List

def maxProfit(prices: List[int]) -> int:
    total = 0

    for i in range(len(prices) - 1):
        if prices[i + 1] - prices[i] > 0:
            total += prices[i + 1] - prices[i]

    return total

arr = [7,6,4,3,1]
result = maxProfit(arr)

print(result)