from book import Book
from bookEx import BookEx, BookEx1, testBookEx


class BookEx2(Book):                               #<---- 1
    def __init__(self, title, author, number):    #<---- 2
        super().__init__(title, author)           #<---- 3
        self.number = number
        Book.count += 1                     #<---- 4

    def printInfo(self):                          #<---- 5
        super().printInfo()                       #<---- 6
        print("   - number : {}".format(self.number))  #<---- 7

def testBookEx1():
    # b1 = Book(title="The Art of Computer Programming", author="도널드 크누스")
    # b2 = Book(title="Design Patterns: Elements of Reusable Object-Oriented Software", author="The 'Gang of Four'")

    # e1 = BookEx(title="The C Programming Language", author="Dennis Ritchie. Brian Kernighan", number = 1)  #<---- 8

    e11 = BookEx2(title="The C ", author="Dennis", number = 2)  #<---- 8

    e11.printInfo()  #<---- 9


if __name__ == '__main__':
    testBookEx()
    testBookEx1()
    c1 = Book(title="The Art of python", author="Hong")
    # c1 = Book(title="The Art", author="HongKs")
    c2 = Book(title="The Art of python", author="Hong1")
    c3 = Book(title="The Art of python", author="Hong1")
    print("Book.count:{}, self.count:{}, c2.count:{}".format(Book.count, c1.count, c2.count))
    print(c3.printFinalCount())
