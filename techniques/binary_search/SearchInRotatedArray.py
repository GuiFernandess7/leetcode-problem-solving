from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int: # ATTEMPT
        r, l = 0, len(nums) - 1

        while r <= l:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[r]:
                if target < nums[r]:
                    l = mid + 1
                elif target > nums[r]:
                    r = mid - 1
                else:
                    return nums[r]

            elif nums[mid] <= nums[l]:
                if target < nums[l]:
                    l = mid + 1
                elif target > nums[l]:
                    r = mid - 1
                else:
                    return nums[l]

        return -1

