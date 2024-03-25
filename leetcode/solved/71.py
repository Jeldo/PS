class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        stack = []
        for p in paths:
            if p == "." or p == "":
                continue
            if p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)


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
