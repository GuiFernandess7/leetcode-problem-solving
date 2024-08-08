def productExceptSelf(nums: int) -> int:
    import math
    prefix_p = [0] * (len(nums) + 1)

    for i in range(0, len(prefix_p)):
        prefix_p[i] = math.prod(nums[:i] + nums[i + 1:])

    return prefix_p[:-1]

arr = [1,2,3,4]
print(productExceptSelf(arr))