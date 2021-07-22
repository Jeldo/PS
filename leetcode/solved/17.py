class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        nums = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        def dfs(combination, d):
            if not d:
                if len(combination) > 0:
                    combinations.append(combination)
                return
            for ch in nums[d[0]]:
                dfs(combination + ch, d[1:])

        combinations = []
        dfs('', digits)

        return combinations


cases = [
    '23',
    '',
    '2',
]

for c in cases:
    res = Solution().letterCombinations(c)
    print(res)
