def totalFruit(fruits) -> int: # Not solved
    baskets = {}

    for fruit in fruits:
        if fruit in baskets:
            baskets[fruit] += 1
        elif len(baskets) > 1:
            break
        else:
            baskets[fruit] = 1

    return baskets

fruits = [1, 2, 3, 2, 2]
result = totalFruit(fruits)
print(result)