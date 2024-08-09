from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    k = 0

    for idx, vec in enumerate(matrix):
        if vec[0] < target < vec[-1]:
            k = idx
        elif vec[-1] == target or vec[0] == target:
            return True

    l, r = 0, len(matrix[k]) - 1
    while l <= r:
        m = l + (r - l) // 2

        if matrix[k][m] == target:
            return True

        if target >= matrix[k][m]:
            l = m + 1
        else:
            l = m - 1

    return False


nums = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
]

print(searchMatrix(nums, 3))