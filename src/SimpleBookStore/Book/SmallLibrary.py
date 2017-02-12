'''
Created on 11 feb. 2017

    SmallLibrary represents a small collection of books, like a
    single person's home collection.
@author: accl
'''


class SmallLibrary(object):

    def __init__(self):

        self.booksInLibrary = []
        self.checkedOut = []

    def buy(self, copy):

        self.booksInLibrary.append(copy)

    def checkOut(self, copy):

        self.booksInLibrary.remove(copy)
        self.checkedOut.append(copy)

    def checkIn(self, copy):

        self.checkedOut.remove(copy)
        self.booksInLibrary.append(copy)

    def isAvailable(self, copy):

        return self.booksInLibrary.count(copy) >= 1

    def find(self, query):

        sol = []
        for copy in self.booksInLibrary:
            if copy.book.title().lower().find(query.lower()) != -1:
                sol.append(copy)
            elif copy.book.author().lower().find(query.lower()) != -1:
                sol.append(copy)
        return sol
