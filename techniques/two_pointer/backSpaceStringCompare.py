def remove_chars(lst):
    result = []
    for char in lst:
        if char == "#":
            if result:
                result.pop()
        else:
            result.append(char)
    return ''.join(result)

def backspaceCompare(s: str, t: str) -> bool:
    s_l = list(s)
    t_l = list(t)

    s_l = remove_chars(s_l)
    t_l = remove_chars(t_l)

    return s_l == t_l

string1 = "ab#c"
string2 = "ad#c"

result = backspaceCompare(string1, string2)
print(result)