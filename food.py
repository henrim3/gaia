class Food:
    def __init__(self, row, column, food):
        self.row = row
        self.col = column
        self.food = food
    
    def __str__(self):
        return "O"
