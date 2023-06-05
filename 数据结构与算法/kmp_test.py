def kmp_match(text, pattern):
    n = len(text)
    m = len(pattern)
    next = get_next(pattern)

    i = 0
    j = 0
    while i < n and j < m:
        if j == -1 or text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            j = next[j]

    if j == m:
        return i - m
    else:
        return -1


def get_next(pattern):
    m = len(pattern)
    next = [-1] * m
    i = 0
    j = -1
    while i < m - 1:
        if j == -1 or pattern[i] == pattern[j]:
            i += 1
            j += 1
            next[i] = j
        else:
            j = next[j]
    return next


print(get_next('asdfasddd'))