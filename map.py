from cell import Cell

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = []
        for r in range(height):
            row = []
            for c in range(width):
                row.append(None)
            self.grid.append(row)
            
    def display(self):
        for row in self.grid:
            for val in row:
                if val:
                    print(val, end="")
                else:
                    print(" ", end="")
            print()
