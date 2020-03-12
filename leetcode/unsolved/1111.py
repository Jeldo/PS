class Solution:
    def maxDepthAfterSplit(self, seq):
        is_A_closed = True
        depth_A, depth_B = 0, 0
        isVPS_A, isVPS_B = 0, 0
        isValid = 0
        answer = list()
        for i in range(0, len(seq)):
            if seq[i] == '(' and is_A_closed == True and isValid == 0:
                answer.append(0)
                is_A_closed = False
            elif seq[i] == ')' and is_A_closed == False and isValid == 0:
                answer.append(0)
                is_A_closed = True
            else:
                if seq[i] == '(':
                    isValid += 1
                else:
                    isValid -= 1
                answer.append(1)
        return answer


seqs = ["(()())", "()(())()", "(((()))((())))"]

# [0,0,1,1,0,0,1,0,0,1,0,0,1,1]
for seq in seqs:
    s = Solution().maxDepthAfterSplit(seq)
    print(s)
