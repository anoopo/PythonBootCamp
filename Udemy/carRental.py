""" program to provide layers of abstraction for a car rental system.
Your program should perform the following:
1. Hatchback, Sedan, SUV should be type of cars that are
being provided for rent
2. Cost per day:
Hatchback - $30
Sedan - $50
SUV - $100
3. Give a prompt to the customer asking him the type of car
and the number of days he would like to borrow and provide the
fare details to the user"""

#Class - RentalSystem
#layer of abstraction - Display the type of cars and the cost per days

#Class - customer
#layer of abstraction -

class RentalSystem:
    cars = {"Hatchback": 30, "Sedan": 40, "SUV":50}
    def displayCars(self):
        print ("Following cars ar available")
        print ("Hatchback = $30")
        print ("Sedan = $40")
        print ("SUC = $50")

    def getTheRentalAmount(self, carType, noOfDays):
        if carType in self.cars.keys():
            return self.cars[carType] * noOfDays
        else:
            print("you have entered a wrong value")
            quit()
class Customer:
    def customMenu(self):
        print (" Enter the following details ")


rent = RentalSystem()
while True:
    print ("Welcome to Rent A Car")
    print ("**** MENU ****")
    print ("1. Display the cars and rates")
    print ("2. Rent a car now")

    mainMenuChoice = int(input())
    if mainMenuChoice == 1:
        rent.displayCars()
    elif mainMenuChoice == 2:
        carType = input("Enter the type of car you would like to rent out")
        noOfDays = int(input("Enter the number of days you would like to rent out"))
        rentAmount = rent.getTheRentalAmount(carType,noOfDays)
        print ("You have to pay", rentAmount, "to rent", carType, "for", noOfDays, "days")
        quit()
    else:
        print ("Wrong choice, quit the menu")
        quit()
