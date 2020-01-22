class Solution:
    def groupThePeople(self, groupSizes):
        answer = list()
        group_dict = dict()
        for i in range(len(groupSizes)):
            if groupSizes[i] not in group_dict.keys():
                group_dict[groupSizes[i]] = list()
            group_dict[groupSizes[i]].append(i)
            if len(group_dict[groupSizes[i]]) == groupSizes[i]:
                answer.append(group_dict[groupSizes[i]])
                del group_dict[groupSizes[i]]
        return answer


groups = [[3, 3, 3, 3, 3, 1, 3], [2, 1, 3, 3, 3, 2]]
for g in groups:
    print(Solution().groupThePeople(g))
