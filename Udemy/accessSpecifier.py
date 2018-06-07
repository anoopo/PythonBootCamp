class Car:
    noOfWheels = 4
    _color = "Black"
    def __init__(self):
        self.__luxury = True
        print ("luxury = ", self.__luxury)

class Bmw(Car):
    def __init__(self):
        print ("Color = ", self._color)

car = Car()
print ("no_of_wheels = ", car.noOfWheels)
print ("color = ", car.__luxury) #use _Car__luxury for this to work
bmw = Bmw()
