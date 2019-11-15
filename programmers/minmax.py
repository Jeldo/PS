def solution(s):
    answer = s.split()
    sol = []
    for x in answer:
        sol.append(int(x))
    return str(min(sol)) + " " + str(max(sol))