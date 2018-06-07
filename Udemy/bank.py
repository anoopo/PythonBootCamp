import msvcrt

class Bank:
    def __init__(self):
        pass

class Menu(Bank):
    def mainMenu(self):
        print ("Enter your choice:")
        print ("1. Sign In (Existing User)")
        print ("2. Sign Up (New User)")
        print ("3. QUIT")
        userChoice = input()
        if userChoice is 1:
            self.signInMenu()
        elif userChoice is 2:
            self.signUpMenu()
        elif userChoice is 3:
            print ("Are you sure to exist (Y/n)?")
            userInput = input()
            if userInput in ["Y/y"]:
                quit()
            else:
                continue
        else:
            continue

class Customer:
    pass

bank = Bank()
menu = Menu()
customer = Customer()

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

menu.mainMenu()
