'''
Created on 11 feb. 2017

@author: accl
'''


class Book(object):
    '''

    Book is an immutable type representing an edition of a book,
    not the physical object, but the combination of words and pictures that
    make up a book. Each book is uniquely identified by its ISBN10 code.

    Attributes:

    title: Title of the book.

    author: Name of the author of the book.

    year: Year when this edition was published in the conventional calendar.
          Must be nonnegative.

    isbn: ISBN-10 code for this edition of the book. Checksum must be correct,
          and raise an exception otherwise.
    '''

    def __init__(self, title, author, year, isbn):
        '''
        Constructor
        '''
        self._title = title
        self._author = author
        self._year = year
        self.isbn = isbn

# isbn checksum must be correct -> using setter on isbn function so an
# exception is raised when an incorrect checksum is provided
    @property
    def isbn(self):
        return self.isbn

    @isbn.setter
    def isbn(self, isbn):
        if self.checkISBN()(isbn):
                    raise Exception("ISBN Checksum is not valid")

    def year(self):
        return self._year

    def title(self):
        return self._title

    def author(self):
        return self._author

    def checkISBN(self):

        return lambda a: (int(a[0]) * 10 +
                          int(a[1]) * 9 +
                          int(a[2]) * 8 +
                          int(a[3]) * 7 +
                          int(a[4]) * 6 +
                          int(a[5]) * 5 +
                          int(a[6]) * 4 +
                          int(a[7]) * 3 +
                          int(a[8]) * 2 +
                          int(a[9])) % 11 != 0
