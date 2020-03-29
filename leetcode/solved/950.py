'''
Array
Time Complexity: O(nlogn)
'''

from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck):
        deck = sorted(deck, reverse=True)        # O(nlogn)
        answer = deque()
        for i in range(0, len(deck)):            # O(n)
            if answer:
                answer.appendleft(answer.pop())  # O(1), O(1)
            answer.appendleft(deck[i])
        return answer


deck = [17, 13, 11, 2, 3, 5, 7]
s = Solution().deckRevealedIncreasing(deck)
print(s)
