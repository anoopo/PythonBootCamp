"""
We want to make a row of bricks that is goal inches long.
We have a number of small bricks (1 inch each) and big bricks (5 inches each).
Return True if it is possible to make the goal by choosing from the given bricks.

make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
make_bricks(3, 2, 6) -> True
"""

"""Algorithm
True if:
 1. goal == totalBricks
 2. Goal <= Small
 3. Goal <= totalBig and goal % 5 == 0
 4. goal - totalBig <= small
 5. goal - Small <= totalBig and (goal - small) % 5 == 0
 """
def make_bricks(small, big, goal):
    totalBig = big *5
    totalBricks = totalBig + small
    if goal == totalBricks:
        print (1)
        return True
    elif goal <= small:
        print (2)
        return True
    elif goal <= totalBig and goal % 5 == 0:
        print (3)
        return True
    elif (goal - totalBig) > 0 and (goal - totalBig) <= small:
        print (4)
        return True
    elif ((goal - small) <= totalBig) and ((goal - small) % 5 == 0):
        print (5)
        return True
    else:
        print (6)
        return False

"""def make_bricks(small, big, goal):
    possibleWithSmallBric ks = [x for x in range(0,small+1)]
    possibleWithLargeBricks = []
    for i in range(1,big+1):
        for j in possibleWithSmallBricks:
            possibleWithLargeBricks.append(j+i*5)
    possibleCombination = possibleWithSmallBricks + possibleWithLargeBricks
    #print (possibleCombination)
    print (goal in possibleCombination)
"""
"""
    big_needed = min(big, goal // 5)
    return goal - (big_needed * 5) <= small
"""
make_bricks(7,9,23)
"""make_bricks(3, 1, 9)
make_bricks(3, 2, 10)
make_bricks(3, 2, 8)
make_bricks(3, 2, 9)
make_bricks(6, 1, 11)
make_bricks(6, 0, 11)
make_bricks(1, 4, 11)
make_bricks(0, 3, 10)
make_bricks(1, 4, 12)
make_bricks(3, 1, 7)
make_bricks(1, 1, 7)
make_bricks(2, 1, 7)
make_bricks(7, 1, 11)
make_bricks(7, 1, 8)
make_bricks(7, 1, 13)
make_bricks(43, 1, 46)
make_bricks(40, 1, 46)
make_bricks(40, 2, 47)
make_bricks(40, 2, 50)
make_bricks(40, 2, 52)
make_bricks(22, 2, 33)
make_bricks(0, 2, 10)
make_bricks(1000000, 1000, 1000100)
make_bricks(2, 1000000, 100003)
make_bricks(20, 0, 19)
make_bricks(20, 0, 21)
make_bricks(20, 4, 51)
make_bricks(20, 4, 39)"""
