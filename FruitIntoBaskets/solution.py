def totalFruit(fruits) -> int:
    baskets = {}
    start = 0
    max_size = 0

    for end in range(len(fruits)):
        if end in baskets:
            baskets[fruits[end]] = 1
        else:
            baskets[fruits[end]] += 1

        while len(baskets) > 2:
            pass

    return baskets

fruits = [1, 2, 3, 2, 2]
result = totalFruit(fruits)
print(result)