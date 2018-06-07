"""Create a class called Square and perform the following tasks -
(i) Create two objects for this class squareOne and
squareTwo
(ii) Find the result of side of squareOne to the power of side
of squareTwo
Example: If squareOne has length of 2cm each side and
squareTwo has a length of 4cm each side, squareOne **
squareTwo should return 16, which is 2 to the power of 4."""

class Square:
    def __init__(self,side):
        self.side = side

    def __pow__(sideOne, sideTwo):
        return (sideOne.side ** sideTwo.side)

squareOne = Square(2)
squareTwo = Square(4)
result = (squareOne ** squareTwo)
print ("result = ", result )
