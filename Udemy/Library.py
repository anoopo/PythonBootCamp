#Class - Library
# layers of abstraction - display the current books, lend a book, add a book

#Class - Customer
# layers of abstraction - request a book, return a book

class Library:
    def __init__(self,listOfBooks):
        self.listOfBooks = listOfBooks

    def displayBooks(self):
        print ("Available books:")
        for book in self.listOfBooks:
            print (book)

    def lendBook(self, bookName):
        if bookName in self.listOfBooks:
            print ("Book is available")
            print ("You have now borrowed the book", bookName)
            self.listOfBooks.remove(bookName)
        else:
            print ("Requested book is not available")
            Library.displayBooks(self)


    def addBook(self, bookName):
        self.listOfBooks.append(bookName)

class Customer:
    def requestBook(self):
        print ("Enter the book you like to borrow:")
        self.book = input()
        return self.book

    def returnBook(self):
        print ("Enter the book you want to return")
        self.book = input()
        return self.book

library = Library(['Suspect X','Notebook','Meluha'])
customer1 = Customer()

while True:
    print ("Menu")
    print ("1. Display the available books")
    print ("2. Request a book")
    print ("3. Return a book")
    print ("4. Quit the menu")

    userChoice = int(input())
    if userChoice is 1:
        library.displayBooks()
    elif userChoice is 2:
        requestedBook = customer1.requestBook()
        library.lendBook(requestedBook)
    elif userChoice is 3:
        returnedBook = customer1.returnBook()
        library.addBook(returnedBook)
    else:
        print ("you have entered a wrong choice")
        quit()
