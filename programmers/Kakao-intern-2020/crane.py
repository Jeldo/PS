def solution(board, moves):
    answer = 0
    stacks = list()
    for j in range(0, len(board[0])):
        temp_stack = list()
        for i in reversed(range(len(board))):
            if board[i][j] != 0:
                temp_stack.append(board[i][j])
        stacks.append(temp_stack)
    stack = list()
    for m in moves:
        if stacks[m-1]:
            cur = stacks[m-1].pop()
            if len(stack) > 0 and cur == stack[-1]:
                stack.pop()
                answer += 1
            else:
                stack.append(cur)
    return answer * 2

cases = [
    [[[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]]
]

for c in cases:
    s = solution(c[0], c[1])
    print(s)