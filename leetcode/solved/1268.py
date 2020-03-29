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

    def suggestedProducts2(self, products, searchWord):
        products = sorted(products)
        ans = list()
        for i in range(1, len(searchWord)+1):
            words = list()
            for p in products:
                isValid = True
                if len(p) < i:
                    continue
                for j in range(i):
                    if searchWord[j] != p[j]:
                        isValid = False
                        break
                if isValid:
                    words.append(p)
                if len(words) == 3:
                    break
            ans.append(words)
        return ans


cases = [
    [["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"],
    [["havana"], "havana"],
    [["bags", "baggage", "banner", "box", "cloths"], "bags"],
    [["havana"], "tatiana"],
    [["hello", "hell"], "helloworld"]
]

for c in cases:
    s = Solution().suggestedProducts2(c[0], c[1])
    print(s)
