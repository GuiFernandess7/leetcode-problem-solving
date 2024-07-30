"""Sum of continuos values within the array"""

from typing import List

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


# ==================================

def findMaxAverage(nums: List[int], k: int) -> float:
    max_avg = float('-inf')
    current_sum = 0

    for i in range(len(nums)):
        current_sum += nums[i]

        if (i >= k - 1):
            new_avg = current_sum / k
            max_avg = max(max_avg, new_avg)
            current_sum -= nums[i- k + 1]

    return max_avg

def findMaxAverage2(nums: List[int], k: int) -> float:
    max_avg = curr_sum = sum(nums[:k])

    for i in range(k, len(nums)):
        curr_sum = curr_sum - nums[i - k] + nums[i]
        max_avg = max(curr_sum, max_avg)

    return max_avg/k

prices = [1,12,-5,-6,50,3]
# ===================================

def maxSubstringSequence(nums: List[int]):
    seen = {}
    longest_seq = 0
    start = 0

    for end in range(len(nums)):
        if nums[end] not in seen:
            seen[nums[end]] = True
            longest_seq = max(longest_seq, end - start + 1)
        else:
            while seen[nums[end]] in seen:
                del seen[nums[end]]
                start += 1

        seen[nums[end]] = True

    return longest_seq

string = "abcabcbb"
#print(maxSubstringSequence(string))

# ==================================

def missingNumber(nums: List[int]) -> int:
    nums.sort()

    if len(nums) == 2 and len(nums) not in nums:
        return len(nums)

    for i in range(len(nums)):
        if i != nums[i]:
            return i

    return 0

nums = [9,6,4,2,3,5,7,0,1]
#result = missingNumber(nums)
#print(result)
