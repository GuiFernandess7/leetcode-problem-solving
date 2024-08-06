def moveZeroes(self, nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    l, r = 0, 0

    while r < n:
        if nums[l] != 0:
            r += 1
            l += 1
        elif nums[r] == 0:
            r += 1
        else:
            nums[r], nums[l] = nums[l], nums[r]
