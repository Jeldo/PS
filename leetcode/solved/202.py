class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        visited.add(n)
        while True:
            new_n = 0
            while n > 0:
                n, q = divmod(n, 10)
                new_n += q ** 2
            if new_n == 1:
                return True
            if new_n in visited:
                return False
            visited.add(new_n)
            n = new_n
