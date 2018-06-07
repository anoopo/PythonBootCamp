from abc import ABCMeta,abstractmethod
from random import randint
import msvcrt

class Account(metaclass = ABCMeta):
    @abstractmethod
    def createAccount():
        return 0

    @abstractmethod
    def verifyAccount():
        return 0

    @abstractmethod
    def withDrawAmount():
        return 0

    @abstractmethod
    def displayAmount():
        return 0

class SavingsAccount(Account):
    def __init__(self):
        self.accountDetails = {}

    def createAccount(self, name, initialDeposit):
        self.accountNumber = randint(10000,100000)
        self.accountDetails[self.accountNumber] = [name,initialDeposit]
        print ("A new account has been created, your account number is",self.accountNumber)

    def verifyAccount(self, name, accountNumber):
        print ()
        if accountNumber in self.accountDetails.keys():
            if self.accountDetails[accountNumber][0] == name:
                print ("User {} successfully authenticated".format(name))
                self.accountNumber = accountNumber
                return True
            else:
                print ()
                print (" *****ERROR: User not found*****")
                print ()
                return False
        else:
            print ()
            print (" *****ERROR: User not found*****")
            print ()
            return False

    def withDrawAmount(self, amount):
        if amount > self.accountDetails[self.accountNumber][1]:
            print ("Funs insufficient in your account")
            self.displayAmount()
        else:
            self.accountDetails[self.accountNumber][1] -= amount
            print ("Withdrawal successful.")
            self.displayAmount()

    def depositAmount(self, amount):
        self.accountDetails[self.accountNumber][1] += amount
        print ("Deposit successful.")
        self.displayAmount()

    def displayAmount(self):
        print ("Your account balance is ", self.accountDetails[self.accountNumber][1])

class Menu():
    def mainMenu(self):
        print ("Enter your choice:")
        print ("1. Sign In (Existing User)")
        print ("2. Sign Up (New User)")
        print ("3. QUIT")
        userChoice = int(input())
        return userChoice

    def optionsMenu(self):
        print ("Enter your choice:")
        print ("1. Withdrawal")
        print ("2. Deposit")
        print ("3. Display")
        print ("4. Go back to previous menu")
        userChoice = int(input())
        return userChoice


savingsAccount = SavingsAccount()
menu = Menu()

def wait():
    print ("press any key to continue...")
    msvcrt.getch()

while True:

    print ("*********************************")
    print ("*    UDEMY BANK WELCOMES YOU    *")
    print ("********************************")
    print (" \n\n\n\n ")
    wait()
    break


while True:
    userChoice = menu.mainMenu()
    if userChoice is 1:
        print ("Enter your details as per the bank records :")
        userName = input("Name :")
        userAccountNumber = int(input("Account Number"))
        signedIn = savingsAccount.verifyAccount(userName,userAccountNumber)
        if signedIn is True:
            while True:
                userOptions = menu.optionsMenu()
                if userOptions is 1:
                    amount = int(input("Enter the amount to be withdrawn:"))
                    savingsAccount.withDrawAmount(amount)
                elif userOptions is 2:
                    amount = int(input("Enter the amount to be deposited"))
                    savingsAccount.depositAmount(amount)
                elif userOptions is 3:
                    savingsAccount.displayAmount()
                elif userOptions is 4:
                    break
                else:
                    continue
    elif userChoice is 2:
        print ("Enter the following details:")
        userName = input("Your name:")
        initialDeposit = int(input("Your initial deposit:"))
        savingsAccount.createAccount(userName,initialDeposit)
    elif userChoice is 3:
        print ("Are you sure to exit (Y/n)?")
        userInput = input()
        if userInput in ("Y","y"):
            quit()
        else:
            continue
