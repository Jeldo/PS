'''
Category: Hash Table
'''


class Solution:
    def replaceWords(self, dictionary: list, sentence: str):
        dictionary = sorted(dictionary)
        res = []
        for w in sentence.split():
            word = ''
            for ch in w:
                word += ch
                if word in dictionary:
                    break
            res.append(word)
        return ' '.join(res)


cases = [
    [["cat", "bat", "rat"], "the cattle was rattled by the battery"],
    [["a", "b", "c"], "aadsfasf absbs bbab cadsfafs"],
    [["a", "aa", "aaa", "aaaa"], "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"],
    [["catt", "cat", "bat", "rat"], "the cattle was rattled by the battery"],
    [["ac", "ab"], "it is abnormal that this solution is accepted"],
]

for c in cases:
    s = Solution().replaceWords(*c)
    print(s)
