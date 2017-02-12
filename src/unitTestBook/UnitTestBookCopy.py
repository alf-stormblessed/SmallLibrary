'''
Created on 11 feb. 2017

@author: accl
'''
import unittest
from SimpleBookStore.Book import BookCopy
from SimpleBookStore.Book import Book
from SimpleBookStore.Book.BookCopy import Condition


class Test(unittest.TestCase):

    def test(self):
        book1 = Book.Book(
                  "The adventures of Sherlock Holmes",
                  "Conan Doyle, Arthur", 1984, "0140623353")

        copy1 = BookCopy.BookCopy(book1)

        assert(copy1.condition == Condition.good)
        assert(copy1.book.title() == "The adventures of Sherlock Holmes")
        assert(copy1.book.year() == 1984)
        assert(copy1.book.author() == "Conan Doyle, Arthur")


if __name__ == "__main__":

    unittest.main()
