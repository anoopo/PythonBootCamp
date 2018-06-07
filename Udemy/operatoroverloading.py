class square:
    def __init__(self, side):
        self.side = side

    def __add__(obj1, obj2):
        return (obj1.side + obj2.side)


obj1 = square(5)
#obj2 = square(10)
print ("Sum of sides of squares = ", obj1+obj2)
