from typing import List

def singleNumber(nums: List[int]) -> int:
    memo = {}

    for n in nums:
        if n not in memo:
            memo[n] = 1

        else:
            memo[n] += 1

    for freq in memo:
        if memo[freq] == 1:
            return freq

def singleNumber(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result

arr = [4,1,2,1,2]
print(singleNumber(arr))