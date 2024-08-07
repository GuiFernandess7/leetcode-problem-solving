def count_groups(weights, max_diff):
    weights.sort()
    n = len(weights)
    count = 0

    start = 0
    for end in range(len(weights)):

        # Expand the end pointer
        while end < n and (weights[end] - weights[start] <= max_diff):
            end += 1

        count += (end - start - 1)

        if end - start > 1:
            count += (end - start - 1)