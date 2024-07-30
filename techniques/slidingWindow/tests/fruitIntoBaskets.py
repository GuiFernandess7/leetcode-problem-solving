from typing import List

def fruitsIntoB(fruits: List[int]) -> int:
    seen = {}
    max_fruits = 0
    start = 0

    for i in range(len(fruits)):
        if fruits[i] not in seen:
            seen[fruits[i]] = 1
        else:
            seen[fruits[i]] += 1

        while len(seen) > 2:
            start_f = fruits[start]
            seen[start_f] -= 1
            if seen[start_f] == 0:
                del seen[start_f]
            start += 1

        max_fruits = max(max_fruits, i - start + 1)

    return max_fruits

if __name__=="__main__":
    fruits = [1,2,3,2,2]
    result = fruitsIntoB(fruits)
    print(result)
