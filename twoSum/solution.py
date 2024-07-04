def two_sum(nums, value):
    cache = {}

    for i, num in enumerate(nums):
        target = value - num
        if target in cache:
            return [cache[target], i]
        cache[num] = i

    return
