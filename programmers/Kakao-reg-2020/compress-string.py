def solution(s):
    min_length = len(s)
    sub = ''
    for i in range(1, len(s)//2+1):
        count = 1
        cur = s[:i]
        for j in range(i, len(s), i):
            if s[j:j+i] == cur:
                count += 1
            else:
                if count == 1:
                    count = ''
                sub += str(count) + cur
                cur = s[j:j+i]
                count = 1
        if count == 1:
            count = ''
        sub += str(count) + cur
        min_length = min(min_length, len(sub))
        sub = ''
    return min_length


cases = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd"
]

for c in cases:
    s = solution(c)
    print(s)
