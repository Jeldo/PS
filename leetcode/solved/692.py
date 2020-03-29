'''
Time Complexity: O(nlogn)
How does it work in O(nlogk) ??
https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity
https://stackoverflow.com/questions/23038756/how-does-heapq-nlargest-work
'''

from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, words, k):
        # O(n) time, O(n) space
        word_dict = Counter(words)
        # O(n)
        word_list = [(-count, word) for word, count in word_dict.items()]
        # O(nlogn)
        return [word for count, word in heapq.nsmallest(k, word_list)]

    def oneliner(self, works, k):
        return [word for count, word in heapq.nsmallest(k, [(-count, word) for word, count in Counter(words).items()])]


words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
s = Solution().topKFrequent(words, k)
print(s)
