def containsNearbyDuplicate(nums: int, k: int) -> bool: # ATTEMPT
    cache = {}
    has_duplicate = False

    for i in range(len(nums)):
        if nums[i] not in cache:
            cache[nums[i]] = i

        elif i - cache[nums[i]] <= k:
            has_duplicate = True

    return has_duplicate

def containsNearbyDuplicate2(nums, k: int) -> bool: # CORRECTION
    cache = {}

    for i in range(len(nums)):
        if nums[i] in cache:
            if i - cache[nums[i]] <= k:
                return True
        cache[nums[i]] = i

    return False

arr = [1,0,1,1]
print(containsNearbyDuplicate(arr, 1))