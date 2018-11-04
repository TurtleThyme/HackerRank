def solve(s):
    prev = ' '
    res = ''
    for i in s:
        if i.isalpha and prev == ' ':
            res += i.upper()
        else:
            res += i
        prev = i
    return res