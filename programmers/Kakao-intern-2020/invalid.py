def solution(user_id, banned_id):
    answer = 0
    return answer


# 2 2 3    
cases = [
    [["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]],
    [["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]],
    [["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]]
]

for c in cases:
    s = solution(c[0], c[1])
    print(s)