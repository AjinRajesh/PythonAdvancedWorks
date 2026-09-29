#Define a class named book with attributes title,author,price,pages,language and
#methods gettitle(),getauthor(),getprice(),settitle(),setauthor(),setprice()
class Book:
    def __init__(self):
        self.title=input("Title: ")
        self.author=input("Enter author: ")
        self.price=int(input("Price: "))
        self.pages=int(input("Pages: "))
        self.lang=input("Language: ")
        print()

    def gettitle(self):
        print("Title:",self.title)

    def getauthor(self):
        print("Author:",self.author)

    def getprice(self):
        print("Price:",self.price)
        print()

    def settitle(self):
        self.title=input("New Title: ")
        self.gettitle()

    def setauthor(self):
        self.author = input("Enter new author: ")
        self.getauthor()

    def setprice(self):
        self.price = int(input("New Price: "))
        self.getprice()
        print()

b=Book()
b.gettitle()
b.getauthor()
b.getprice()
b.settitle()
b.setauthor()
b.setprice()
