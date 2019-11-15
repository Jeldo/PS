def solution(arrangement):
    prior = None
    parentheses = 0
    count = 0 
    for p in arrangement:
        if prior == "(" and p == ")":
            parentheses -= 1
            count += parentheses
        elif prior == ")" and p == ")":
            parentheses -= 1
            count += 1
        else:
            parentheses += 1
        prior = p
    return count