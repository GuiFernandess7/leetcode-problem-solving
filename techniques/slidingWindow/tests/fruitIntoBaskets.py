from typing import List

def fruitsIntoB(fruits: List[int]) -> int:
    seen = set()
    max_fruits = 0
    start = 0

    for i in range(len(fruits)):
        if fruits[i] not in seen or len(seen) < 3:
            seen.add(fruits[i])
            max_fruits = max(max_fruits, i - start + 1)

        elif len(seen) >= 3:
            while fruits[i] in seen:
                seen.remove(fruits[i])
                start += 1

    return max_fruits

if __name__=="__main__":
    fruits = [1, 2, 1]
    result = fruitsIntoB(fruits)
    print(result)
