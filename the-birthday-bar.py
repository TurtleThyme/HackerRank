def birthday(s, d, m):
    place_holder = 0
    for i in range(len(s) - m + 1):
        a = 0
        for j in range(i, i + m):
            a = a + s[j]
        if a == d:
            place_holder += 1
    return place_holder
