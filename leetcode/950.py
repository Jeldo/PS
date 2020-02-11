from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck):
        deck = sorted(deck, reverse=True)
        answer = deque()
        for i in range(0, len(deck)):
            if answer:
                answer.appendleft(answer.pop())
            answer.appendleft(deck[i])
        print(type(answer))
        return answer


deck = [17, 13, 11, 2, 3, 5, 7]
s = Solution().deckRevealedIncreasing(deck)
print(s)
