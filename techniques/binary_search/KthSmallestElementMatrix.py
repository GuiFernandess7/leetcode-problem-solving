from typing import List

def kthSmallest(matrix: List[List[int]], k: int) -> int:
    def flat_matrix(matrix): # O(n)
        res = []

        for m in matrix:
            res += m

        return res

    res = flat_matrix(matrix)
    res.sort()

    if len(matrix) >= 1:
        return res[k - 1]
    return res[k]

arr = [[-5]] #[[1,5,9],[10,11,13],[12,13,15]]
k = 1

print(kthSmallest(arr, k))