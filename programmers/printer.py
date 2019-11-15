def solution(priorities, location):
    isChecked = [False]*len(priorities)
    max_num = max(priorities)
    count = 0
    idx = 0
    while isChecked[location] == False:
        if priorities[idx] == max_num and isChecked[idx] == False:
            count += 1
            isChecked[idx] = True
            priorities[idx] = 0
            max_num = max(priorities)
            
        idx += 1
        if idx == len(priorities):
            idx = 0
            
    return count