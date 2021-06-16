# O(N*M), M= length of A
def solution2(N, A):
    counters = [0] * N
    max_num = 0
    for num in A:
        if num == N + 1:
            counters = [max_num] * N
        elif num <= N:
            counters[num-1] += 1
            max_num = max(max_num, counters[num-1])
    return counters


def solution(N, A):
    result = [0]*N    # The list to be returned
    max_counter = 0   # The used value in previous max_counter command
    current_max = 0   # The current maximum value of any counter
    for command in A:
        if 1 <= command <= N:
            # increase(X) command
            if max_counter > result[command-1]:
                # lazy write
                result[command-1] = max_counter
            result[command-1] += 1
            if current_max < result[command-1]:
                current_max = result[command-1]
        else:
            # max_counter command
            # just record the current maximum value for later write
            max_counter = current_max
    for index in range(0, N):
        if result[index] < max_counter:
            # This element has never been used/updated after previous
            #     max_counter command
            result[index] = max_counter
    return result


cases = [
    [5, [3, 4, 4, 6, 1, 4, 4]]
]


for c in cases:
    res = solution(*c)
    print(res)
