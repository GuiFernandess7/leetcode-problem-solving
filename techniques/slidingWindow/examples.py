"""Sum of continuos values within the array"""

def best_brute_force(prices, k): # O(nk)
    max_total = 0

    for i in range(len(prices) - k + 1):
        total_sum = sum(prices[i: i + k])
        max_total = max(max_total, total_sum)

    return max_total

def sliding_window(prices, k): # O(n)
    total = sum(prices[:k])
    max_total = total

    for i in range(len(prices) - k):
        total -= prices[i]
        total += prices[i + k]
        max_total = max(max_total, total)

    return max_total


prices = [15, 7, 31, 30, 21, 22, 19, 17, 24, 27, 50, 26, 33, 6, 22, 17, 42, 21, 17, 37, 49, 31, 37]
print(best_brute_force(prices, 5))