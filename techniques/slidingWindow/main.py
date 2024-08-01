"""Sum of continuos values within the array"""

from typing import List

def best_brute_force(prices, k): # O(nk)
    max_total = 0

    for i in range(len(prices) - k + 1):
        total_sum = sum(prices[i: i + k])
        max_total = max(max_total, total_sum)

    return max_total

def sliding_window(prices, k): # O(n)
    """Biggest Sum - Fixed Sliding Window"""

    total = sum(prices[:k])
    max_total = total

    for i in range(len(prices) - k):
        total -= prices[i]
        total += prices[i + k]
        max_total = max(max_total, total)

    return max_total

def sliding_window_2(prices, k=3):
    """Biggest sum - Fixed sliding window # 2"""
    max_value = float('-inf')
    current_sum = 0

    for i in range(len(prices)):
        current_sum += prices[i]
        if (i >= k - 1):
            max_value = max(max_value, current_sum)
            current_sum -= prices[i - (k - 1)]

    return max_value

def dynamic_sliding_window(target_sum, arr):
    """Min size window with target sum"""
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
    """Max substring with non repeating characters"""
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

def maxSubstringSequence2(nums: List[int]):
    charset = set()
    longest_substring = 0
    l = 0

    for i in range(len(nums)):
        while nums[i] in charset:
            charset.remove(nums[i])
            l += 1

        charset.add(nums[i])
        longest_substring = max(longest_substring, i - l + 1)
    return longest_substring

string = "abcabcbb"

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

#=================================

def fruitIntoBackets(fruits: List[int]):
    max_fruits = 0
    seen = {}
    start = 0

    for end in range(len(fruits)):
        if fruits[end] not in seen:
            seen[fruits[end]] = 1
        else:
            seen[fruits[end]] += 1

        while len(fruits) < 2:
            left_fruit = fruits[start]
            fruits[left_fruit] -= 1
            if fruits[left_fruit] == 0:
                del fruits[left_fruit]
            start += 1

        max_fruits = max(max_fruits, end - start + 1)

    return max_fruits

fruits = [1, 2, 1]
#result = fruitIntoBackets(fruits)
#print(result)

# ============================

def string_permutation_attempt(s1: str, s2: str): # two pointer approach
    from collections import Counter
    has_permutation = False
    s1 = Counter(s1)

    mid = len(s2) // 2
    right = mid
    left = 0

    while left < mid or right < len(s2):
        if left < mid:
            current_slice = s2[left:right+1]
            left += 1
        elif right < len(s2):
            current_slice = s2[mid:right+1]
            right += 1

        if s1 == Counter(current_slice):
            has_permutation = True

    return has_permutation

def string_permutation(s1: str, s2: str):
    from collections import Counter
    has_permutation = False
    k = len(s1)
    s1 = Counter(s1)

    for right in range(len(s2)):
        if right >= k - 1:
            current_slice = s2[right - k + 1:right + 1]
            if s1 == Counter(current_slice):
                has_permutation = True

    return has_permutation

string = "eidbaooo"
#results = string_permutation("ba", string)
#print(results)

# ===============================

def characterReplacement(s: str, k: int):
    start = 0
    seen = set()
    s = list(s)

    for end in range(len(s) - 1):
        if s[end] not in seen:
            seen.add(s[end])

            if k >= 0 :
                s[end] = s[start]
                k -= 1

        else:
            while s[end] in seen:
                seen.remove(s[end])
            start += 1

    return len(s[end - start + 1:end + 1])

string = "AABABBA"
result = characterReplacement(string, 2)
print(result)