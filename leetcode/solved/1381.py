'''
Category: Stack, Design
'''


class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.stack = []

    def push(self, x: int):
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self):
        if 0 < len(self.stack):
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int):
        for i in range(min(len(self.stack), k)):
            self.stack[i] += val
