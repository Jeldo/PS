class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowel = set('aeiouAEIOU')
        result = []
        for i, w in enumerate(sentence.split()):
            if w[0] not in vowel:
                w = w[1:] + w[0]
            result.append(w + 'ma' + 'a' * (i + 1))

        return ' '.join(result)


cases = [
    "I speak Goat Latin",
    "The quick brown fox jumped over the lazy dog",
]

for c in cases:
    print(Solution().toGoatLatin(c))
