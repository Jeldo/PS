class SubrectangleQueries:

    def __init__(self, rectangle):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int):
        for r in range(row1, row2 + 1):
            for c in range(col1, col2 + 1):
                self.rectangle[r][c] = newValue

    def getValue(self, row: int, col: int):
        return self.rectangle[row][col]

    def print_rectangle(self):
        for i in range(len(self.rectangle)):
            for j in range(len(self.rectangle[0])):
                print(self.rectangle[i][j], end=' ')
            print()
