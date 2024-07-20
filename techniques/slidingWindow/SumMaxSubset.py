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

def sliding_window_2(prices, k):
    max_value = float('-inf')
    current_sum = 0

    for i in range(len(prices)):
        current_sum += prices[i]
        if (i >= k - 1):
            max_value = max(max_value, current_sum)
            current_sum -= prices[i - (k - 1)]

    return max_value

def dynamic_sliding_window(target_sum, arr):
    min_window_size = float('inf')
    current_window_sum = 0
    window_start = 0

    for window in range(len(arr)):
        current_window_sum += arr[window]

        while current_window_sum >= target_sum:
            min_window_size = min(min_window_size, window - window_start + 1)
            current_window_sum -= arr[window_start]
            window_start += 1

    return min_window_size

prices = [15, 7, 31, 30, 21, 22, 19, 17, 24, 27, 50, 26, 33, 6, 22, 17, 42, 21, 17, 37, 49, 31, 37]
print(dynamic_sliding_window(76, prices))