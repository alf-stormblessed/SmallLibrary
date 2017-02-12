'''
Created on 11 feb. 2017

@author: accl
'''
import unittest
from SimpleBookStore.Book import Book


class Test(unittest.TestCase):

    def testIncorrectIsbn(self):

        # incorrect ISBN checksum
        self.assertRaises(Exception, Book.Book,
                          "The adventures of Sherlock Holmes",
                          "Conan Doyle, Arthur", 1984, "1140623353")

    def testCorrectIsbn(self):

        # correct ISBN checksum
        Book.Book(
                  "The adventures of Sherlock Holmes",
                  "Conan Doyle, Arthur", 1984, "0140623353")

    def testGetters(self):

        book = Book.Book(
                "The adventures of Sherlock Holmes",
                "Conan Doyle, Arthur", 1984, "0140623353")

        assert(book.author() == "Conan Doyle, Arthur", "incorrect author")
if __name__ == "__main__":

    unittest.main()
