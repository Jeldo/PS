from itertools import permutations


class Solution:
    # 1 dfs
    def numTilePossibilities(self, tiles: str):
        result = set()

        def dfs(path, tile):
            print(path)
            if path not in result:
                if path:
                    result.add(path)
                for i in range(0, len(tile)):
                    dfs(path+tile[i], tile[:i]+tile[i+1:])
        dfs('', tiles)
        return len(result)

    # 2 brute force using permutation
    def numTilePossibilities2(self, tiles: str):
        tile_set = set()
        for i in range(1, len(tiles)+1):
            for p in permutations(tiles, i):
                s = ''.join(p)
                if s not in tile_set:
                    tile_set.add(s)
        return len(tile_set)


s = Solution().numTilePossibilities("AABC")
print(s)
