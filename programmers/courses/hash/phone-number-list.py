class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def __repr__(self):
        return str(self.children)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if cur.end:
                return False
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True
        return True


def solution(phone_book):
    answer = True
    t = Trie()
    for p in sorted(phone_book):
        answer = t.insert(p)
        if not answer:
            break
    return answer


def solution2(phone_book):
    answer = True
    d = set()
    for p in phone_book:
        # d[p] = 1
        d.add(p)
    for p in phone_book:
        temp = ''
        for n in p:
            temp += n
            if temp in d and temp != p:
                answer = False
    return answer


cases = [
    ['119', '97674223', '1195524421'],
    ['123', '456', '789'],
    ['12', '123', '1235', '567', '88'],
    ['45', '4'],
    ['4', '45'],
]

for c in cases:
    s = solution2(c)
    print(s)
