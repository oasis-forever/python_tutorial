from shape import Shape

class Square(Shape):
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        dimension = self.side * 4
        return dimension

    def change_size(self, diff):
        return (self.side + diff) * 4
