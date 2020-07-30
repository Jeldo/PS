'''
Category: String
'''


class Solution:
    def removeSubfolders(self, folder: list):
        folder.sort()
        pool = []
        for f in folder:
            if not pool or not f.startswith(pool[-1] + '/'):
                pool.append(f)
        return pool


cases = [
    ["/a", "/a/b", "/c/d",  "/c/f", "/c/d/e"],
    ["/a", "/a/b/c", "/a/b/d"],
    ["/a/b/c", "/a/b/ca", "/a/b/d"]
]

for c in cases:
    s = Solution().removeSubfolders(c)
    print(s)
