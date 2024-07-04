from typing import List

def rotate(nums: List[int], k: int) -> None:
    k = k % len(nums)

    def rotate(start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    rotate(0, len(nums) - 1)
    rotate(0, k - 1)
    rotate(k, len(nums) - 1)

    return nums


nums = [-1, -100, 3, 99]
nums2 = [1,2,3,4,5,6,7]
print(rotate(nums2, k=3))