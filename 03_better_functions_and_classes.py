
# Functions
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# always try to create small functions that does one and only one task

# first write the code that implemetns the functionality, and once you
 # have implemented the feature and it works, you can start thinking about
 # breaking the function into multiple functions for clearer code

 # generators are functions that use the yeild keyword
 # they are useful for two main reasons

 # 1) when generators call functions, they immediately return the iterator
 # instead of running the whole function, on which you can perform different
 # acions like looping or converting to a list
 # once you are dont, it automatically calls the built-in function next()
 # and goes back to the calling function on the next line after the yield
 # keyword. It also makes your code eaasier to read and understand

 # 2) in a list or another data structure, python needs to save the data in
 # memory before returning, which can cause a memory crash if the data
 # turns out to be large. A generator does not have this issue. So, when
 # you have a large amount of data to process or you are not sure about
 # the size of data beforehand, it is recommended to use a generator instead of
 # another data structure

 # if you know the size or the size of return data is not large like 100 emails
 # then returning a list or tuple is fine
 # ------------------------------------------------------------------------------

 # use keyword arguments
 # ------------------------------------------------------------------------------
 # force a keyword argument into a caller function by defining the functions as follows
 def spam_email(from, *, to, subject, size, sender_name, reciever_name):
     pass

# Logging
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Import logging module
# code doesnt work with setting levels defo check this module out
import logging

logger = logging.getLogger(__name__)          # Create a custom logger
handler = logging.StreamHandler               # Using stream handler

# Set logging levels
handler.setLevel(logging.WARNING)
handler.setLevel(logging.ERROR)

format_c = logging.Formatter("%(name) - %(levelname) - %(message)")
handler.setFromatter(format_c)                     # Add formater to handler
logger.addHandler(handler)

def division(divident, divisor):
    try:
        return divident/divisor
    catch ZeroDivisionError:
        logger.error("Zero Division Error")

num = divison(4, 0)
# ------------------------------------------------------------------------------
# Unit Test
#-------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# py.test and unittest
# you can use unit test as documentation for the code which can be helpful
# when you revisit the code
# it gives you a sense of confidence that your code does the expected behavior
# it prevents old bugs from creeping into your code
import unittest

def sum_numbers(x, y):
    return x + y

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_numbers(3, 4), 7)

# pytest
def test_sum_numbers():
    assert func(3, 4) == 7
# ------------------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# while writing a class always remember the single responsibility principle
# Duplicate code and your class doing more than 1 thing is a sign that
# the class is too big and should be broken down
# Class structure
# ------------------------------------------------------------------------------

# Class vars
# want these at the top as they are either constants or default variables
# this shows the developer that these are ready to use

# __init__
# constructor

# built in python special methods -> __call__, __repr__
# special methods change the default behaviour of the class or give extra
# functionality to a class, so having them top of a class makes the reader
# of the class aware of some customized features of the class
# metaclasses are being overiden and give you an idea of what a class is trying
# to do something different bu changing the usual behaviour of the python class

# class methods
# a class method works as another constructor, so keeping it near __init__
# makes sense. It tells the developer other ways the class can be used without
# creating a constructor using __init__

# static methods
# a static method is bound to the class and not the object of the class like
# class methods. They cant modify the class state, so it makes sense to add them
# at the top to make reader aware of the methods that are used for specific purposes

# instance methods
# instance methods add behaviour in a class, keeping them after special methods
# makes it easier for a reader to understand the code

# private methods

# ------------------------------------------------------------------------------
class Employee(Person):
    POSITIONS = ("Superwiser", "Manager", "CEO", "Founder")

    def __init__(self, name, id, department):
        self.name = name
        self.id = id
        self.department = department
        self.age = None
        self._age_last_calculated = None
        self._recalculated_age()

    def __str__(self):
        return ("Name: " + self.name + "\nDepartment: "
               + self.department)

    @classmethod
    def no_position_allowed(cls, position):
        return [t for t in cls.POSITIONS if t != position]


    @staticmethod
    def c_positions(position):
        return [t for t in cls.TITLES if t in position]

    @property
    def id_with_name(self):
        return self.id, self.name

    def age(self):
        if (datetime.date.today() > self._age_last_recalculated):
            self.__recalculated_age()
        return self.age


    def _recalculated_age(self):
        today = datetime.date.today()
        age = today.year - self.birthday.year
        if today < datetime.date(
           today.year, self.birthday.month,
           self.birthday.year):
	     age -= 1
        self.age = age
        self._age_last_recalculated = today

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------


# When to use static methods
# ------------------------------------------------------------------------------
# static methods are related to classes but dont need to access any class-specific
# date. You dont use self or cls in a static method
# these methods can work on their own without having any dependency on the class
# state. This is one of the main reasons for getting confused when using static
# methods instead of stand-alone functions
# so if the method is related to the class even though it doesnt use any of the
# class vars etc then it can still be a good idea to put it inside the class
# as a static method

# with static use
# ------------------------------------------------------------------------------
class BookPriceCalculator:
    PER_PAGE_PRICE = 8

    def __init__(self, pages, author):
        self.pages = pages
        self.author = author

    @property
    def standard_price(self):
        return self.pages * PER_PAGE_PRICE


    @staticmethod
    def price_to_book_ratio(market_price_per_share, book_value_per_share):
        return market_price_per_share/book_value_per_share
# ------------------------------------------------------------------------------

# without static use
# ------------------------------------------------------------------------------
def price_to_book_ratio(market_price_per_share, book_value_per_share):
    return market_price_per_share/book_value_per_share

class BookPriceCalculator:
    PER_PAGE_PRICE = 8

    def __init__(self, pages, author):
        self.pages = pages
        self.author = author

    @property
    def standard_price(self):
        return self.pages * PER_PAGE_PRICE
# ------------------------------------------------------------------------------

# Use abstract class inheritance the pytonic way
# ------------------------------------------------------------------------------
# the main purposes of having a abstract class in your interface
# you can make an interface class using abstraction
# it can make it impossible to use an interface without implementing
# abstract methods
# it gives early errors if you do not adhere to abstract class rules

# python has a module called 'adc' which does what you expect from an abstract class
# ------------------------------------------------------------------------------
from abc import ABCMeta, abstractmethod

class Fruite(metaclass=ABCMeta):

    @abstractmethod
    def taste(self):
        pass

    @abstractmethod
    def originated(self):
        pass


class Apple:
    def originated(self):
        return "Central Asia"


fruite = Fruite("apple")
"""
TypeError:
"Can't instantiate abstract class concrte with abstract method taste"
"""
from abc import ABCMeta, abstractmethod

class Fruite(metaclass=ABCMeta):

    @abstractmethod
    def taste(self):
        pass

    @abstractmethod
    def originated(self):
        pass


class Apple:
    def originated(self):
        return "Central Asia"


fruite = Fruite("apple")
"""
TypeError:
"Can't instantiate abstract class concrte with abstract method taste"
"""
# ------------------------------------------------------------------------------


# Use @classmethod to access class state
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# a class method gives you the flexibility to creatte alternative constructors
# besides using the __init__ method
# a place to use this would be to create multiple constructors by passing a
# class object, so it is one of the easiest ways to create a factory pattern in
# python
# ------------------------------------------------------------------------------
class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def using_string(cls, names_str):
        first, second = map(str, names_str.split(""))
        student = cls(first, second)
        return Student

    @classmethod
    def using_json(cls, obj_json):
        # Parsing json object…
        return Student

    @classmethod
    def using_file_obj(cls, file_obj):
       # Parsing file object…
       return Student


data = User.using_string("Larry Page")
data = User.using_json(json_obj)
data = User.using_file_obj(file_obj)
# ------------------------------------------------------------------------------
