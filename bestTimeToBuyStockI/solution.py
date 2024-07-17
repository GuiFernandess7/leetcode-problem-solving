from typing import List
import sys

def maxProfit(prices: List[int]) -> int:
    min_price = float('inf')
    max_price = 0

    for price in prices:
        if price < min_price:
            min_price = price

        if price - min_price > max_price:
            max_price = price - min_price

    return max_price

prices = [7, 1, 5, 3, 6, 4]
prices2 = [7,6,4,3,1]
result = maxProfit(prices)
print(result)

