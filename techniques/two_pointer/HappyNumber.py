def isHappy(n: int) -> bool:
    while n != 1:
       digits = [int(digit) for digit in str(n)]
       squared_digits = list(map(lambda x: x * x, digits))
       n = sum(squared_digits)
    return digits # FAILED


def isHappy(n: int) -> bool:
    def get_sum_of_squares(num: int) -> int:
        return sum(int(digit) ** 2 for digit in str(num))

    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        n = get_sum_of_squares(n)

    return n == 1


n = 195
print(isHappy(n))