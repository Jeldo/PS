'''
Category: String
'''
from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: list):
        file_dict = defaultdict(list)
        for d in paths:
            data = d.split()
            base_dir, files = data[0], data[1:]
            for f in files:
                s = f.split('(')
                name, content = s[0], s[1][:-1]
                file_dict[content].append('{}/{}'.format(base_dir, name))
                # print(name, content)
        return [v for v in file_dict.values() if len(v) > 1]


cases = [
    ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)",
     "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"],
    ["root/a 1.txt(abcd) 2.txt(efsfgh)", "root/c 3.txt(abdfcd)",
     "root/c/d 4.txt(efggdfh)"]
]

for c in cases:
    s = Solution().findDuplicate(c)
    print(s)
