from collections import Counter

def substring_palindrome(string: str):
    res = 0

    for i in range(len(string)):
        l = r = i
        while l >= 0 and r < len(string) and string[l] == string[r]:
            res += 1
            l -= 1
            r += 1


l = "abbaacc"
result = substring_palindrome(l)
