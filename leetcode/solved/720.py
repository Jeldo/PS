class Node:
    def __init__(self, ch: str):
        self.ch = ch
        self.children = dict()
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = Node('')
        self.root.is_end = True
        self.longest_word = ''

    def insert(self, word: str):
        node = self.root
        for i, ch in enumerate(word):
            if ch in node.children:
                node = node.children[ch]
            elif i == len(word) - 1:
                new_node = Node(ch)
                node.children[ch] = new_node
                node = new_node
            else:
                return

        node.is_end = True

    def get_longest_word(self):
        head = self.root

        def dfs(node: Node, longest_word: str):
            if not node.children:
                if len(self.longest_word) < len(longest_word):
                    self.longest_word = longest_word
                return
            for ch in node.children:
                dfs(node.children[ch], longest_word + ch)

        dfs(head, '')
        return self.longest_word


class Solution:
    def longestWord(self, words: list[str]) -> str:
        words.sort()
        word_set = set()
        word_set.add('')
        longest_word = ''
        for word in words:
            if word[:-1] in word_set:
                if len(longest_word) < len(word):
                    longest_word = word
                word_set.add(word)

        return longest_word

    def longestWord2(self, words: list[str]) -> str:
        words.sort()
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.get_longest_word()


cases = [
    ["w", "wo", "wor", "worl", "world"],
    ["a", "banana", "app", "appl", "ap", "apply", "apple"],
    ["a", "banana", "app", "appl", "ap", "apple", "apply"],
    ['a', 'app'],
    ["yo", "ew", "fc", "zrc", "yodn", "fcm", "qm", "qmo", "fcmz", "z", "ewq", "yod", "ewqz", "y"],
]

for c in cases:
    print(Solution().longestWord(c))
