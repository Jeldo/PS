class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path.replace('//', '/')
        for p in path.split('/'):
            if p:
                if stack and p == '..':
                    stack.pop()
                elif p != '..' and p != '.':
                    stack.append(p)
        if not stack:
            return '/'
        return '/' + '/'.join(stack)


cases = [
    "/home/",
    "/../",
    "/home//foo/",
    "/a/./b/../../c/",
    "/../../../",
    "/a/../../b/../c//.//",
]

for c in cases:
    print(Solution().simplifyPath(c))
