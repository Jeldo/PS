'''
Category: Hash Table
'''
from collections import defaultdict


class Solution:
    def displayTable(self, orders: list):
        table = defaultdict(dict)
        menu = set()
        for o in orders:
            if o[2] not in menu:
                menu.add(o[2])
            if o[2] not in table[int(o[1])]:
                table[int(o[1])][o[2]] = 1
            else:
                table[int(o[1])][o[2]] += 1
        menu = sorted(menu)
        result = [['0'] * (len(menu) + 1) for _ in range(len(table) + 1)]
        result[0] = ['Table'] + menu
        idx = 1
        for k in sorted(table.keys()):
            result[idx][0] = str(k)
            idx += 1
        for i in range(1, len(result)):
            for j in range(1, len(result[0])):
                if result[0][j] in table[int(result[i][0])].keys():
                    result[i][j] = str(table[int(result[i][0])][result[0][j]])
        return result


cases = [
    [
        ["David", "3", "Ceviche"],
        ["Corina", "10", "Beef Burrito"],
        ["David", "3", "Fried Chicken"],
        ["Carla", "5", "Water"],
        ["Carla", "5", "Ceviche"],
        ["Rous", "3", "Ceviche"]
    ],
    [
        ["James", "12", "Fried Chicken"],
        ["Ratesh", "12", "Fried Chicken"],
        ["Amadeus", "12", "Fried Chicken"],
        ["Adam", "1", "Canadian Waffles"],
        ["Brianna", "1", "Canadian Waffles"]
    ],
    [
        ["Melissa", "2", "Soda"],
        ["Laura", "2", "Bean Burrito"],
        ["Jhon", "2", "Beef Burrito"],
    ]
]

for c in cases:
    s = Solution().displayTable(c)
    print(s)
