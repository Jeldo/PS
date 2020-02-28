class Solution:
    def fairCandySwap(self, A, B):
        sumA = sum(A)
        sumB = sum(B)
        each = (sumA+sumB)//2
        targetA = sumA - each
        targetB = sumB - each
        
        print(each)
        for i in range(0, len(A)):
            for j in range(0, len(B)):
                #3
                3

AA = [1, 2, 5]
BB = [2, 4]

sol = Solution()
print(sol.fairCandySwap(AA, BB))
