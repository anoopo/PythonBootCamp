class Furniture:
    def __init__(self):
        self.typeOfWood = "TeakWood"

class Chair(Furniture):
    #def __init__(self):
    __noOfLegs = 4

    def setWoodType(self, typeOfWood):
        self.typeOfWood = typeOfWood

    def chairChara(self):
        print ("Chair has {} legs and is made of {}".format(self.__noOfLegs,self.typeOfWood))

chair = Chair()
print ("Do you want to change the make of chair from TeakWood to something else? (Y/n)")
userInput = input()
if userInput in ("YyYes"):
    print ("Enter the wood type you like to use")
    userType = input()
    chair.setWoodType(userType)
chair.chairChara()
