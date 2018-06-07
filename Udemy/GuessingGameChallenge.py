"""
Write a program that picks a random integer from 1 to 100,
and has players guess the number. The rules are:

1. If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
2. On a player's first turn, if their guess is
    a) within 10 of the number, return "WARM!"
    b) further than 10 away from the number, return "COLD!"
3. On all subsequent turns, if a guess is
    a) closer to the number than the previous guess return "WARMER!"
    b) farther from the number than the previous guess, return "COLDER!"
4. When the player's guess equals the number,
   tell them they've guessed correctly and how many guesses it took!
"""

from random import randint


printprint(("WELCOME TO GUESS ME!""WELCOM )
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

def getTheResult(guessedList,rand):
    if len(guessedList) == 1:
        if guessedList[0] < 10:
            return "WARM....try again"
        else:
            return "COLD....try again"
    else:
        if guessedList[-1] <= guessedList[-2]:
            return "WARMER...almost there"
        else:
            return "COLDER...try again"

while True:
    results = []
    numberOfGuesses = 0
    randomNumber = randint(1,100)
    print (randomNumber)
    while numberOfGuesses < 3:
        numberOfGuesses += 1
        print (numberOfGuesses)
        userChoice = int(input("Enter your number : "))
        result = abs(userChoice-randomNumber)
        results.append(result)
        if result == 0:
            print ("Congratulations! You Win in {} guesses".format(numberOfGuesses))
            break
        else:
            print (getTheResult(results,randomNumber))
    else:
        print ("GAME OVER - 3 guesses expired")


    while True:
        userChoice = input("Do you want to start the game again (Y/n)")
        if userChoice in ("N","n","No"):
            print ("Thank You! Please come again")
            quit()
        elif userChoice in ("Y","y","Yes"):
            break
        else:
            print ("Wrong Choice")
