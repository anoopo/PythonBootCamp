class MusicalInstruments:
    noOfKeys = 12
    name = "MI"

class StringInstruments(MusicalInstruments):
    typeOfWood = "ToneWood"
    name = "SI"

class Guitar(StringInstruments):
    def __init__(self):
        print ("noofKeys = ",self.noOfKeys)
        print ("typeofwood = ",self.typeOfWood)
        print ("name = ",MusicalInstruments.name)

guitar1 = Guitar()
