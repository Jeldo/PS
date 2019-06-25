class Solution:
    def heightChecker(self, heights):
        h =  sorted(heights)
        count = 0
        for i  in range(0, len(h)):
            if h[i] != heights[i]:
                count +=1 
        return count


ins = [1, 1, 4, 2, 1, 3]
sol = Solution()
print(sol.heightChecker(ins))
