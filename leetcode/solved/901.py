'''
Category: Stack
Time Complexity: Amortized O(1) (Worst: O(n))
'''


class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int):
        day = 1
        while self.stack and self.stack[-1][0] <= price:
            day += self.stack.pop()[1]
        self.stack.append((price, day))
        return day


cases = [
    [100, 80, 60, 70, 60, 75, 85],  # 1 1 1 2 1 4 6
    [29, 91, 62, 76, 51]  # 1 2 1 2 1
]

for c in cases:
    s = StockSpanner()
    for i in c:
        print(s.next(i), end=' ')
    print()
