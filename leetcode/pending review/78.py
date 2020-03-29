from itertools import combinations


class Solution:
    # implement combination
    def subsets(self, nums):
        def comb(lst, n):
            if n == 0:
                return [[]]
            l = []
            for i in range(0, len(lst)):
                m = lst[i]
                remainder = lst[i+1:]
                for p in comb(remainder, n-1):
                    l.append([m]+p)
            return l
        subs = list()
        for i in range(0, len(nums)+1):
            subs.extend(comb(nums, i))
        return subs

    # using library
    def subsets2(self, nums):
        subs = list()
        for i in range(0, len(nums)+1):
            for c in combinations(nums, i):
                subs.append(list(c))
        return subs

    def subsets3(self, nums):
        n = len(nums)
        output = [[]]
        for num in nums:
            output += [curr + [num] for curr in output]
        return output

    def subsets4(self, nums):
        n = len(nums)
        output = []
        for i in range(2**n, 2**(n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            print(bitmask)
            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        return output

    def subsets5(self, nums):
        def backtrack(first=0, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output


nums = [
    [1, 2, 3],
    [1, 2, 3, 4]
]

for n in nums:
    s = Solution().subsets4(n)
    print(s)
