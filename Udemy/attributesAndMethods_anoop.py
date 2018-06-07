class PreciousStone:
    stones = []
    numberOfStones = 0
    def addStones(self,stone):
        self.stone = stone
        PreciousStone.numberOfStones += 1
        if PreciousStone.numberOfStones <=5:
            PreciousStone.stones.append(self.stone)
        else:
            del PreciousStone.stones[0]
            PreciousStone.stones.append(self.stone)


    def displayStones(self):
        for stone in PreciousStone.stones:
            print (stone)

newstone = PreciousStone()
newstone.addStones("Ruby")
newstone.addStones("Emerald")
newstone.addStones("Ruby")
newstone.addStones("Emerald")
newstone.addStones("Ruby")
newstone.addStones("Emerald")
newstone.displayStones()
