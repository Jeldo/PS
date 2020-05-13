def solution(skill, skill_trees):
    count = 0
    skill_set = set(skill)
    for s in skill_trees:
        checker = ''
        for ch in s:
            if ch in skill_set:
                checker += ch
        is_skill = True
        for i in range(min(len(skill), len(checker))):
            if skill[i] != checker[i]:
                is_skill = False
        if is_skill:
            count += 1
    return count


cases = [
    ("CBD", ["BACDE", "CBADF", "AECB", "BDA"])
]


for c in cases:
    s = solution(c[0], c[1])
    print(s)
