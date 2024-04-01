class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        num_to_letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []

        def dfs(letters, digit):
            if not digit:
                if letters:
                    result.append(letters)
                return
            for ch in num_to_letter[digit[0]]:
                dfs(letters + ch, digit[1:])
        dfs("", digits)
        return result


cases = [
    "23",
    "",
    "2",
]

for c in cases:
    print(Solution().letterCombinations(c))
