class OperatingSystem:
    multiTasking = True
    name = "Mac OS"

class Apple:
    website = "www.apple.com"
    name = "Apple"

class MacBook(Apple,OperatingSystem):
    def __init__(self):
        if self.multiTasking is True:
            print ("This OS supports multiTasking. Visit {} for more details".format(self.website))
            print ("Name = ", self.name)
mac = MacBook()
