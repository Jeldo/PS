from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.maxLength = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
            return
        if len(self.cache) == self.maxLength:
            # remove LRU one
            self.cache.popitem(False)
        self.cache[key] = value


class LRUCacheInDict:
    def __init__(self, capacity: int):
        self.maxLength = capacity
        self.cache = dict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
            return
        if len(self.cache) == self.maxLength:
            del self.cache[next(iter(self.cache))]
        self.cache[key] = value


cases = [
    [
        ["LRUCache", "put", "put", "get", "put",
            "get", "put", "get", "get", "get"],
        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
    ],
    [
        ["LRUCache", "get", "put", "get", "put", "put", "get", "get"],
        [[2], [2], [2, 6], [1], [1, 5], [1, 2], [1], [2]],
    ],
    [
        ["LRUCache", "put", "put", "put", "put", "get", "get"],
        [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]]
    ]
]

for c in cases:
    # cache: LRUCache = None
    cache: LRUCacheInDict = None
    for k, v in zip(c[0], c[1]):
        if k == 'LRUCache':
            cache = LRUCache(v[0])
        elif k == 'get':
            res = cache.get(v[0])
            print(res)
        elif k == 'put':
            cache.put(v[0], v[1])
    print()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# obj = LRUCache(2)
# obj.put(1, 1)
# obj.put(2, 2)
# res = obj.get(1)
# print(res)
# obj.put(3, 3)
# res = obj.get(2)
# print(res)
# obj.put(4, 4)
# res = obj.get(1)
# print(res)
# res = obj.get(3)
# print(res)
# res = obj.get(4)
# print(res)
