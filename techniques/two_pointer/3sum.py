from typing import List

# Attempt Failed
def threeSum(nums: List[int]) -> List[List[int]]:
    l, r = 0, len(nums) - 1
    seen = {}

    total_sum = sum(nums)
    result = []

    while l < r:
        if l != r:
            curr_sum = total_sum - nums[l] + nums[r]

            if nums[l] not in seen:
                seen[nums[l]] = l
            if nums[r] not in seen:
                seen[nums[r]] = r

            if (curr_sum) in seen:
                result.append([total_sum - curr_sum, nums[l], nums[r]])

        l += 1
        r -= 1

    return result

def threeSum2(nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    l, r = 0, len(nums) - 1
    seen = {}
    result = []

    while l < r:
        curr_value = nums[l] + nums[r]
        value3 = - curr_value

        if value3 in seen:
            result.append([value3, nums[l], nums[r]])

        if nums[l] not in seen:
            seen[nums[l]] = l
        if nums[r] not in seen:
            seen[nums[r]] = r

        l += 1
        r -= 1

    return result

def threeSum3(nums):
    nums = sorted(nums)
    left = 0
    right = len(nums) - 1
    seen_values = set()
    result = []

    while left < right:
        total = nums[left] + nums[right]
        missing_value = -total

        if missing_value in seen_values:
            result.append([nums[left], nums[right], missing_value])

        seen_values.add(nums[left])
        seen_values.add(nums[right])

        if total < 0:
            left += 1
        elif total > 0:
            right -= 1
        else:
            left += 1
            right -= 1

    return result

def threeSum4(nums):
    nums = sorted(nums)
    left = 0
    right = len(nums) - 1
    seen = set()
    memo = {}
    result = []
    k = 0

    while left < right:
        curr_sum = nums[left] + nums[right]
        k = - curr_sum

        if nums[left] not in seen:
            memo[nums[left]] = left
        if nums[right] not in seen:
            memo[nums[right]] = right

        if curr_sum < 0:
            left += 1
        elif curr_sum > 0:
            right -= 1
        else:
            right -= 1
            left += 1

        if k in memo:
            result.append([k, nums[left], nums[right]])

    return result

arr = [-1,0,1,2,-1,-4]
result = threeSum4(arr)
print(result)
# [[1, 0, -1]]