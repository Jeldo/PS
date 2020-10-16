'''
Backtracking, DFS
'''


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        results = set()

        def dfs(path: str, tile: str):
            nonlocal results
            if path not in results:
                if path:
                    results.add(path)
                for i in range(len(tile)):
                    dfs(path+tile[i], tile[:i] + tile[i+1:])

        dfs('', tiles)
        return len(results)


cases = [
    'AAB',
    'AAABBC',
    'V'
]

for c in cases:
    s = Solution().numTilePossibilities(c)
    print(s)
