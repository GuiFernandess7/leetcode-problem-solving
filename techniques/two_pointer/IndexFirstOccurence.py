def strStr(haystack: str, needle: str) -> int:
    n = len(needle)

    for i in range(len(haystack) + 1 - n): # REMINDER
        if haystack[i:i+n] == needle:
            return i

    return -1

haystack = "hello"
needle = "ll"

print(strStr(haystack, needle))