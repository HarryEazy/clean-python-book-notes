
# SETS
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# use sets for speed
# they dont allow dupes
# you cant access set elements using an index
# set can access elements in O(1) time since they use hash tables
# sets dont allow some common operations that lists do like slicing and lookups
# sets can sort the elements at insertion time
#
# whenever you dont need these functionalities consider using a set
# because it will make your code much faster
# sets are useful when you need to access items frequently
# ------------------------------------------------------------------------------

# NAMES TUPLES
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# a namedtuple is a tuple ith the name of the data
# has extra features compared with a tuple
# named tupe makes your code more pythonic
# if you are not going to change the values then consider using a namedtuple

# examples
# ------------------------------------------------------------------------------
from collections import namedtuple

# Make a namedtuple
Company = namedtuple("Company", ["name", "employee", "location"])

# Assing values
company = Company("google", 50000, "MountainView")

# Get values
company.name
#>>> google
company.employee
#>>> 50000
company.location
#>>> MountainView
#-------------------------------------------------------------------------------
# can use a namedtuple instead of a class
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
#-------------------------------------------------------------------------------
import namedtuple


Point = namedtuple("Point", ["x", "y", "z"])
point = Point(x=3, y=4, z=5)
point.x
point.y
point.z
#-------------------------------------------------------------------------------
# Return data
# usually you would use a tuple to return data, however, you should consider
# using a namedtuple because it makes code much more readable
# if you have multiple values to return you migh consider using a dict or tuple
# however, tuple have no contect as to the data in them and a dict is mutable
# so a namedtuple works well here as it is immutable and provides context as to
# the information it holds
# you can also convert a namedtuple to a dict or a list to a namedtuple
# so they are flexible
#-------------------------------------------------------------------------------
def get_user_info(user_obj):
    user = get_data_from_db(user_obj)
    UserInfo = namedtuple(“UserInfo”, [“first_name”, “last_name”, “age”])

    user_info = UserInfo(first_name=user[“first_name”],
                         last_name=user[“last_name”],
                         age=user[“age”])

    return user_info

def get_full_name(user_info):
    return user_info.first_name + user_info.last_name

user_info = get_user_info(user_obj)
full_name = get_full_name(user_info)
#-------------------------------------------------------------------------------

Understanding STR, UNICODE & BYTE
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# str is a representation type of a string in python
# Unicode gives you unique identification to each character in all languages
# U+ 0000 (four digits)
# Unicode assigns a numerical ID called a code point to each character so you
# have an unambiguous reference
# when you map any character to a bit pattern, it is called encoding (ASCII) &
# UTF-8
# python interpreters use UTF-8
# ------------------------------------------------------------------------------

# Use List carefully and prefer generators
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# generators are a useful feature of pyton because they make you code performant
# for data-intensive worl
# a generator also forces you to think about making the code more readable
# read more on this!
# ------------------------------------------------------------------------------

# Use zip to process a list
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# when you have two lists and you want to process them in parallel, consider
# using 'zip', this is an inbuilt function and very efficient
# ------------------------------------------------------------------------------
# so instead of the below
def get_user_salary_info():
    users = get_users_name_from_db()
    # ["Abe", "Larry", "Adams", "John", "Sumit", "Adward"]

    users_salary = get_users_salary_from_db()
    #  ["2M", "1M", "60K", "30K", "80K", "100K"]

    users_salary = []
    for index in len(users):
        users_salary.append([users[index], users_salary[index]])

    return users_salary
# ------------------------------------------------------------------------------
# use zip
def get_user_salary_info():
    users = get_users_name_from_db()
    # ["Abe", "Larry", "Adams", "John", "Sumit", "Adward"]

    users_salary = get_users_salary_from_db()
    #  ["2M", "1M", "60K", "30K", "80K", "100K"]

    users_salary = []
    for usr, slr in zip(users, users_salary):
        users_salary.append(usr, slr)

    return users_salary
# ------------------------------------------------------------------------------

# Take advantage of python's built-in function
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# below is a list to check out
# collections
# has useful data structures like namedtuple, defaultDict etc
# CSV
# for reading and writing CSV files
# datetime and time
# math
# re -> regular expressions
# tempfile -> create temporary files
# itertools -> permutations and combinations
# functools -> functional programming - lots of functions that will help
# you to think of your code in a more functional way
# sys and os -> OS level operations
# subprocess -> create multiple processes on your system
# logging -> adds logs to your system
#json
# pickle ->serialize and deserialize a python object
# __future__ -> pseudomodule enables new language features that are not
# compatible with the current interpreter
# ------------------------------------------------------------------------------

# Dictionary and collections
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# collections has a number of interfaces that are really useful for performing
# different tasks with a dictionary

# Counter
# ------------------------------------------------------------------------------
# gives you a convenient way to tally up similar data
# works well with dictionaries
# has useful methods like most_common()
# ------------------------------------------------------------------------------
# Deque
# if you need to create a queue or a stack
# allows you to append or pop from the right or the left
# make dequeue
deq = deque('abcdefg')
# ------------------------------------------------------------------------------
# Default Dict
# a default dict is initilised with function('default factory')
# which takes no arguments and provides the default value for a nonexistent key
# it doesnt raise a KeyError like a dict, any key that doesnt exist gets the value
# returned by the default factory

# make default dict
from collections import defaultdict
colours = defaultdict(int)
# ------------------------------------------------------------------------------
# Switch statement using dictionary
# python doesnt have a switch keyword but you cna use a dict instead
# Example to show, how switch can be implimented, not working example.
def tanzania(amount):
    calculate_tax = <Tax Code>
    return calculate_tax

def zambia(amount):
    calculate_tax = <Tax Code>
    return calculate_tax

def eritrea(amount):
    calculate_tax = <Tax Code>
    return calculate_tax


contry_tax_calculate = {
	"tanzania": tanzania,
            "zambia": zambia,
   	"eritrea": eritrea,
}

def calculate_tax(country_name, amount):
    country_tax_calculate["contry_name"](amount)


calculate_tax("zambia", 8000000)
# ------------------------------------------------------------------------------
# Merge two dictionaries

salary_first = {"Lisa": 238900, "Ganesh": 8765000, "John": 3450000}
salary_second = {"Albert": 3456000, "Arya": 987600}
salary = salary_first.copy()
salary.update(salary_second)
# ------------------------------------------------------------------------------
# Pretty Printing a dict
import pprint

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(colors)
# ------------------------------------------------------------------------------
