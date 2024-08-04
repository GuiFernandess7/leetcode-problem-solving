def two_sum(nums, value):
    cache = {}

    for i, num in enumerate(nums):
        target = value - num
        if target in cache:
            return [cache[target], i]
        cache[num] = i

    return

def twoSum2(numbers, target: int):
    cache = {}

    for i, num in enumerate(numbers):
        complement = target - num
        if complement in cache:
            return [cache[complement], i]
        cache[num] = i

    return None

arr = [2,7,11,15]
result = twoSum2(arr, 9)
print(result)


