def max_subarray(nums):
    curr_sum = 0
    n = len(nums)
    max_sum = float('-inf')

    for i in range(n):
        curr_sum += nums[i]
        max_sum = max(curr_sum, max_sum)
        if curr_sum < 0:
            curr_sum = 0

    return max_sum

