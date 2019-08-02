
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
        #return self.x == other.x and\
        #    self.y == other.y
        if self.x == other.x and\
            self.y == other.y:
            return True
        else:
            return False
    def __add__(self, other):
        # ***etgar:
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(3.5, 8.8)
#print(p1.__repr__())
p2 = Point(5.9, 10.1) # 50
#print(p2)
p3 = Point(5.9, 10.1) # 60
#p2 = p3 # p2 = 60
print('Point equal ? ',p2 == p3)
#print(p2 == (3, 4))

# MobilePhone
# __init__ (self, brand,
#             model, price)
#   data - brand, model, price
# __rerp__, __str__, __eq__
# ** etgar __add__, __gt__:
#   return total price
# *** etgar: Point __add__
#   returns a point(x1+y1,x2+y2)
class MobilePhone():
    def __init__(self, brand,
             model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def __repr__(self):
        return f'MobilePhone({self.brand}, {self.model}, {self.price})'
    def __str__(self):
        return f'MobilePhone: brand = {self.brand} model = {self.model} price = {self.price}'
    def __eq__(self, other):
        if self.brand == other.brand\
            and self.model == other.model\
            and self.price == other.price:
            return True
        else:
            return False
    def __add__(self, other):
        return self.price + other.price
    def __gt__(self, other):
        #return self.price > other.price
        if self.price > other.price:
            return True
        else:
            return False

iphoneX = MobilePhone("Apple",
    "IPhoneX", 3500)
iphoneX11 = MobilePhone("Apple",
    "IPhoneX", 3500)
print('phone equals? ',iphoneX == iphoneX11)
print(iphoneX11 + iphoneX)
samsung = MobilePhone("Samsung",
    "S9+", 4000)
print(samsung > iphoneX)

