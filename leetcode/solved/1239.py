from typing import List

# O(2^n), where N is the maximum length of a string in arr.


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def is_unique(s):
            return len(set(s)) == len(s)

        def dfs(arr: List[str], path: str, i: int):
            nonlocal max_length
            if is_unique(path):
                max_length = max(max_length, len(path))
            if i == len(arr) or not is_unique(path):
                return
            for j in range(i, len(arr)):
                dfs(arr, path + arr[j], j + 1)

        max_length = 0
        dfs(arr, "", 0)
        return max_length


cases = [
    ["un", "iq", "ue"],
    ["cha", "r", "act", "ers"],
    ["abcdefghijklmnopqrstuvwxyz"],
]

for c in cases:
    print(Solution().maxLength(c))
