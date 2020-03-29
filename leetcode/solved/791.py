class Solution:
    def customSortString(self, S, T):
        def find(s, ch):
            return [i for i, ltr in enumerate(s) if ltr == ch]
        T = sorted(T)
        answer = str()
        is_checked = [False] * len(T)
        for ch in S:
            idxes = find(T, ch)
            for i in idxes:
                answer += T[i]
                is_checked[i] = True
        for i in range(len(is_checked)):
            if not is_checked[i]:
                answer += T[i]
        return answer


S = "cba"
T = "abcd"

SS = "cbafg"
TT = "abcd"  # cbad

SSS = "kqep"
TTT = "pekeq"

s = Solution().customSortString(SSS, TTT)
print(s)
