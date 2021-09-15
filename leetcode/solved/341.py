class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flatten_list = []
        self.index = 0

        def dfs(nested_list: [NestedInteger]):
            for x in nested_list:
                if x.isInteger():
                    self.flatten_list.append(x.getInteger())
                else:
                    dfs(x.getList())

        dfs(nestedList)

    def next(self) -> int:
        n = self.flatten_list[self.index]
        self.index += 1
        return n

    def hasNext(self) -> bool:
        return self.index < len(self.flatten_list)
