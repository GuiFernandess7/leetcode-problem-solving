def maxArea(height) -> int:
    n = len(height)
    l, r = 0, n - 1
    max_area = 0

    if len(height) == 2:
        return min(height[0], height[1])

    while r != l:
        distance = r - l
        curr_height = min(height[r], height[l])
        max_area = max(max_area, distance * curr_height)

        if height[l] >= height[r]:
            r -= 1
        else:
            l += 1

    return max_area

height = [1, 1]#[1,8,6,2,5,4,8,3,7] # [4,3,2,1,4] #[1,8,6,2,5,4,8,3,7]
result = maxArea(height)
print(result)
