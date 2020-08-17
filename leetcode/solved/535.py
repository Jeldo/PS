'''
Category: Hash Table
'''
import hashlib


class Codec:
    def __init__(self):
        self.table = dict()

    def encode(self, longUrl: str):
        hs = hashlib.sha1(longUrl.encode())
        hs = hs.hexdigest()
        if hs not in self.table:
            self.table[hs] = longUrl
        return hs

    def decode(self, shortUrl: str):
        return self.table[shortUrl]


cases = [
    'https://leetcode.com/problems/design-tinyurl'
]

for c in cases:
    codec = Codec()
    s = codec.decode(codec.encode(c))
    print(s)
