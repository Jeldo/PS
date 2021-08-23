from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_index = defaultdict(set)
        guess_index = defaultdict(set)
        bulls, cows = 0, 0

        for i, n in enumerate(secret):
            secret_index[n].add(i)
        for i, n in enumerate(guess):
            guess_index[n].add(i)

        for ch in secret_index.keys():
            if ch in guess_index:
                bull = secret_index[ch].intersection(guess_index[ch])
                bulls += len(bull)
                left = secret_index[ch] - bull
                right = guess_index[ch] - bull
                if left and right:
                    cows += min(len(left), len(right))

        return f'{bulls}A{cows}B'


cases = [
    ["1807", "7810"],  # 1A3B
    ["1123", "0111"],  # 1A1B
    ['1', '0'],  # 0A0B
    ['1', '1'],  # 1A0B,
    ['11', '11'],
    ['11', '00'],
    ['01', '10'],
    ['2121', '1212']
]

for c in cases:
    print(Solution().getHint(*c))
