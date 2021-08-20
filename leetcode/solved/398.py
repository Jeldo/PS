from collections import defaultdict


class Solution:

    def __init__(self, nums: list[int]):
        self.num_index = defaultdict(list)
        self.cur_index = dict()
        for i, n in enumerate(nums):
            self.num_index[n].append(i)
            self.cur_index[n] = 0

    def pick(self, target: int) -> int:
        result = self.num_index[target][self.cur_index[target]]
        self.cur_index[target] = (self.cur_index[target] + 1) % len(self.num_index[target])
        return result

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
