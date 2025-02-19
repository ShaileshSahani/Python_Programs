class SHAPE:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rectangle(self):
        print("Rectangle: ", self.x * self.y)


class CIRCLE(SHAPE):
    def square(self):
        print("Square: ", self.x * self.x)


obj = CIRCLE(10, 20)
obj.rectangle()
obj.square()
