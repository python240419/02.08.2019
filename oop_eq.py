
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
    def __eq__(self, other):
        if self.x == other.x and\
            self.y == other.y:
            return True
        else:
            return False

p1 = Point(3.5, 8.8)
#print(p1.__repr__())
p2 = Point(5.9, 10.1) # 50
#print(p2)
p3 = Point(5.9, 10.1) # 60
#p2 = p3 # p2 = 60
print(p2 == p3)
#print(p2 == (3, 4))

# MobilePhone
# __init__ (self, brand,
#             model, price)
#   data - brand, model, price
# __rerp__, __str__, __eq__

