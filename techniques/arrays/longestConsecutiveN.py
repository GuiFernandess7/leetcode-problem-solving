def longestConsecutive(nums: int) -> int: # ATTEMPT
    nums.sort()
    count = 0

    if not nums:
        return 0

    for end in range(len(nums)):
        if nums[end] == nums[end - 1] + 1:
            count += 1

    return count

def longestConsecutive(nums: int) -> int: # CORRECTION
    if not nums:
        return 0

    nums.sort()

    current_length = 1
    longest = 0

    for end in range(1, len(nums)):
        if nums[end] == nums[end - 1]:
            continue
        if nums[end] == nums[end - 1] + 1:
            current_length += 1
        else:
            current_length = 1

    current_length = max(current_length, longest)

    return longest

