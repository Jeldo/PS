'''
Category: String
Time Complexity: O(nlogn)
'''


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

    def customSortString2(self, S: str, T: str):
        S_counter, T_counter = Counter(S), Counter(T)
        intersection = S_counter & T_counter
        sub = set(T) - set(S)
        answer = ''
        for k in intersection.keys():
            answer += k * T_counter[k]
        for x in sub:
            answer += x * T_counter[x]
        return answer


cases = [
    ['cba', 'abcd'],
    ['fhg', 'zxc'],
    ["kqep", "pekeq"]
]

for c in cases:
    s = Solution().customSortString(c[0], c[1])
    print(s)
