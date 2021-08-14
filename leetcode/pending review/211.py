from collections import defaultdict


class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.end = False


class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.end = True

    def search(self, word):
        node = self.root
        exist = False

        def dfs(node: Node, word):
            nonlocal exist
            if not word:
                if node.end:
                    exist = True
                return
            if word[0] == '.':
                for n in node.children.values():
                    dfs(n, word[1:])
            else:
                node = node.children[word[0]]
                if not node:
                    # character does not exist in children
                    return
                dfs(node, word[1:])

        dfs(node, word)
        return exist


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

cases = [
    [
        ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"],
        [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]
    ],
    [
        ["WordDictionary", "addWord", "addWord", "addWord", "addWord", "addWord", "search", "search", "search",
         "search", "search", "search", "search"],  # F T T T T T F
        [[], ["bad"], ["dad"], ["mad"], ["mgd"], ["mcf"], ["pad"], ["bad"], [".ad"], ["b.."], ["..d"], [".c."], ["dcf"]]
    ],
    [["WordDictionary", "search"], [[], ["a"]]],
    [["WordDictionary",
      "addWord", "addWord", "addWord", "addWord", "search",
      "search", "addWord", "search", "search",
      "search", "search", "search", "search"],
     [[],
      ["at"], ["and"], ["an"], ["add"], ["a"],
      [".at"], ["bat"], [".at"], ["an."],
      ["a.d."], ["b."], ["a.d"], ["."]]]
]

for c in cases:
    res = []
    for command, word in zip(c[0], c[1]):
        if command == 'WordDictionary':
            d = WordDictionary()
            res.append(None)
        elif command == 'addWord':
            d.addWord(word[0])
            res.append(None)
        elif command == 'search':
            res.append(d.search(word[0]))
    print(res)
