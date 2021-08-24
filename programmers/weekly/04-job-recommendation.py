from collections import defaultdict


def solution(table, languages, preference):
    language_scores = defaultdict(dict)
    job_types = dict()
    for t in table:
        category = t.split()
        job_types[category[0]] = 0
        for i, language in enumerate(category[1:]):
            language_scores[category[0]][language] = 5 - i

    for l, p in zip(languages, preference):
        for job_type in job_types.keys():
            if l in language_scores[job_type]:
                job_types[job_type] += language_scores[job_type][l] * p

    job_type = ''
    score = 0
    for k, v in job_types.items():
        if v > score:
            score = v
            job_type = k
        elif v == score and k < job_type:
            job_type = k

    return job_type


cases = [
    [
        ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
         "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
         "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5],
    ],
    [
        ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
         "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
         "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5],
    ]
]

for c in cases:
    print(solution(*c))
