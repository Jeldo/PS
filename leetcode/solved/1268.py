'''
Category: String
Time Complexity: O(nlogn * logn) - Bisect
'''
import bisect


class Solution:
    def suggestedProducts(self, products, searchWord):
        products = sorted(products)
        ans = list()
        for i in range(1, len(searchWord)+1):
            words = list()
            for p in products:
                if searchWord[:i] == p[:i]:
                    words.append(p)
                if len(words) == 3:
                    break
            ans.append(words)
        return ans

    def suggestedProducts2(self, products: list, searchWord: str):
        answer = []
        for i in range(1, len(searchWord)+1):
            word = searchWord[:i]
            candidates = []
            for product in products:
                if product.startswith(word):
                    candidates.append(product)
            answer.append(sorted(candidates)[:3])
        return answer

    # Binary Search
    def suggestedProducts3(self, products, searchWord):
        products.sort()
        cur, ans = '', []
        for char in searchWord:
            cur += char
            i = bisect.bisect_left(products, cur)
            ans.append([product for product in products[i: i + 3]
                        if product.startswith(cur)])
        return ans

    # Trie
    def suggestedProducts4(self, products, searchWord):
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.suggestions = list()

        class Trie:
            def __init__(self):
                self.root = self.getNode()

            def insert(self, word):
                node = self.root
                for ch in word:
                    if ch not in node.children:
                        node.children[ch] = TrieNode()
                    node = node.children[ch]
                    if len(node.suggestions) < 3:
                        node.suggestions.append(word)

            def search(self, searchWord):
                res = list()
                node = self.root
                for ch in searchWord:
                    if node:
                        node = node.children.get(ch, None)
                    res.append(node.suggestions if node else [])
                return res

        trie = Trie()
        for p in sorted(products):
            trie.insert(p)
        ans = trie.search(searchWord)
        return ans


cases = [
    [["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"],
    [["havana"], "havana"],
    [["bags", "baggage", "banner", "box", "cloths"], "bags"],
    [["havana"], "tatiana"],
    [["hello", "hell"], "helloworld"]
]

for c in cases:
    s = Solution().suggestedProducts4(c[0], c[1])
    print(s)
