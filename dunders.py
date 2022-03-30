class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y


v1 = Vector(3, 5)
v2 = Vector(2, 7)
print(v1 * v2)
