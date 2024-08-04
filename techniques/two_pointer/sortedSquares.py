from typing import List

def sortedSquares(nums: List[int]) -> List[int]:
    r = len(nums) - 1
    l = 0
    result = []
    squared = list(map(lambda x: x * x, nums))

    for i in range(len(squared)):
        if squared[r] > squared[l]:
            result.append(squared[r])
            r -= 1
        else:
            result.append(squared[l])
            l += 1

    result.reverse()
    return result

arr = [-4,-1,0,3,10]
print(sortedSquares(arr))