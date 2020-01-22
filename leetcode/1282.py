'''
Greedy
Time Complexity: O(n)
'''


class Solution:
    def groupThePeople(self, groupSizes):
        # 1<= len(groupSizes) <= 500
        # 1<= groupSizes[i] <= len(groupSizes)
        answer = list()
        group_dict = dict()
        for i in range(len(groupSizes)):  # O(n)
            if groupSizes[i] not in group_dict.keys():  # O(1)
                group_dict[groupSizes[i]] = list()
            group_dict[groupSizes[i]].append(i)  # O(1)
            if len(group_dict[groupSizes[i]]) == groupSizes[i]:
                answer.append(group_dict[groupSizes[i]])
                del group_dict[groupSizes[i]]  # O(1)
        return answer


groups = [[3, 3, 3, 3, 3, 1, 3], [2, 1, 3, 3, 3, 2]]
for g in groups:
    print(Solution().groupThePeople(g))
