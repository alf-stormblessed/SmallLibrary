'''
Created on 11 feb. 2017

@author: accl
'''
import unittest
from SimpleBookStore.Book import SmallLibrary
from SimpleBookStore.Book import BookCopy
from SimpleBookStore.Book import Book


class TestSmallLibrary(unittest.TestCase):

    def testIsAvailable(self):

        library = SmallLibrary.SmallLibrary()
        book1 = Book.Book(
            "The adventures of Sherlock Holmes",
            "Conan Doyle, Arthur", 1984, "0140623353")

        copy1 = BookCopy.BookCopy(book1)
        copy2 = BookCopy.BookCopy(book1)
        library.buy(copy1)

        assert(library.isAvailable(copy1))
        assert(not library.isAvailable(copy2))

    def testCheckInOut(self):

        library = SmallLibrary.SmallLibrary()
        book1 = Book.Book(
            "The adventures of Sherlock Holmes",
            "Conan Doyle, Arthur", 1984, "0140623353")

        copy1 = BookCopy.BookCopy(book1)
        copy2 = BookCopy.BookCopy(book1)
        library.buy(copy1)
        library.buy(copy2)

        library.checkOut(copy1)
        assert(not library.isAvailable(copy1))
        assert(library.isAvailable(copy2))

        library.checkIn(copy1)
        assert(library.isAvailable(copy1))

    def testCheckFind(self):

        library = SmallLibrary.SmallLibrary()
        book1 = Book.Book(
            "The adventures of Sherlock Holmes",
            "Conan Doyle, Arthur", 1984, "0140623353")

        book2 = Book.Book(
            "The Colour Of Magic",
            "Pratchett, Terry", 2012, "0552166596")
        copy1 = BookCopy.BookCopy(book1)
        copy2 = BookCopy.BookCopy(book2)
        library.buy(copy1)
        library.buy(copy2)

        assert(copy1 not in library.find("magic"))
        assert(copy2 in library.find("magic"))

        assert(copy1 not in library.find("terry"))
        assert(copy2 in library.find("terry"))

        assert(copy1 not in library.find("python"))
        assert(copy2 not in library.find("python"))

if __name__ == "__main__":

    unittest.main()
