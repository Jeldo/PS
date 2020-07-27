class Solution:
    def exclusiveTime(self, n: int, logs: list):
        stack, result = [], []
        lasted = 0
        for l in logs:
            log = l.split(':')
            pid, state, time = int(log[0]), log[1], int(log[2])
            if state == 'start':
                stack.append((pid, time))
            elif state == 'end':
                start_pid, start_time = stack.pop()
                print((start_pid, start_time), (pid, time))
                lasted = time - start_time + 1 - lasted
                result.append(lasted)
        return sorted(result)


cases = [
    [2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]],  # 3, 4
    [4, ["0:start:0", "1:start:1", "2:start:2", "2:end:3",
         "1:end:4", "3:start:6", "3:end:7", "0:end:8"]],     # 3, 2, 2, 2
    [2, ["0:start:0", "0:start:2", "1:start:3", "1:end:5"]]  # 3, 3
]

for c in cases:
    s = Solution().exclusiveTime(c[0], c[1])
    print(s)
