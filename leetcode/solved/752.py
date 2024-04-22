class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        visited = set()

        q = deque([("0000", 0)])
        while q:
            n, count = q.popleft()
            if n == target:
                return count
            if n in deadends or n in visited:
                continue
            visited.add(n)
            for i in range(4):
                for d in [-1, 1]:
                    digit = (int(n[i])+d) % 10
                    new_n = n[:i] + str(digit) + n[i+1:]
                    q.append((new_n, count + 1))

        return -1
