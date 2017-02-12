'''
Created on 11 feb. 2017

@author: accl
'''
from enum import Enum


class Condition(Enum):
    good = "Good"
    damaged = "Damaged"


class BookCopy(object):
    '''
    classdocs
    BookCopy is a mutable type representing a particular copy of a book that is
    held in a library's collection.

    By creating a new BookCopy object it creates a copy of the book,
    initially in good condition.
    - book: the Book of which this is a copy
    - condition: Condition of the book that can be good(1) or damaged(2)
    '''

    def __init__(self, book):
        '''
        Constructor
        '''
        self.book = book
        self.condition = Condition.good
