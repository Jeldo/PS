class RandomizedSet:

    def __init__(self):
        self.data_index = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.data_index:
            return False
        self.data_index[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data_index:
            return False
        element_index_to_remove = self.data_index[val]
        last_element = self.data[-1]
        self.data_index[last_element] = element_index_to_remove
        self.data[element_index_to_remove] = last_element
        self.data.pop()
        self.data_index.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
