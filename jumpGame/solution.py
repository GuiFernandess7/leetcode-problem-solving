from typing import List

def canJump(nums: List[int]):
    jumps = 0

    for n in nums:
        if jumps < 0 :
            return False

        elif n > jumps:
            jumps = n

        jumps -= 1

    return True

arr =  [2, 3, 1, 1, 4]

# n = 3 | jumps = 3
# n = 2 | jumps = 2
# n = 1 | jumps = 1
# n = 0 | jumps = 0

print(canJump(arr))