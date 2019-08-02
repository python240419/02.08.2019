
# class Point
# __init__(self, x, y)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # str - 1st priority
    # repr - developers
    def __repr__(self):
        return f'Point({self.x}, ' \
            f'{self.y})'
    def __str__(self):
        return f'Point x={self.x} y={self.y}'

p1 = Point(3.5, 8.8)
print(p1.__repr__())
p2 = Point(5.9, 10.1)
print(p2)
