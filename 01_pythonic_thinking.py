
# private methods start with '_'
# double '__' to prevent name mangling with other functions

# wrong way
def get_user_info(id):

# right way
# makes it more clear what this function is for and what is the param
# much more readable
def get_user_by(user_id):

# expressions and statements

# its not always worth being smart and doing things in 1 line
# below is an example of sorting a nested dict in 1 line with lambda and the
# better way
users = [
    {"first_name": "Helen", "age": 39},
    {"first_name": "Buck", "age": 10},
    {"name": "anni", "age": 9}
    ]

# bad way
users = sorted(users. key=lambda user: user['first_name'].lower())

# good way
def get_user_name(users):
    """Get name of the user in lower case"""
    return users["first_name"].lower()

def get_sorted_dictionary(users):
    """Sort the nested dictionary"""
    if not isinstance(users, dict):
        raise ValueError("Not a correct dictionary")
    if not len(users):
        raise ValueError("Empty dictionary")

    users_by_name = sorted(users, key=get_user_name)
    return users_by_name


# breaking code into helper functions makes complex code more readable
# and easier to debug when you hit an error

# here this code has a lot going on and thus makes it harder to debug
# better to split some of the functionality of the below code
import csv

# bad way
with open("employee.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
            print(f'\t{row["name"]} salary: {row["salary"]}'
                  f'and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')


# good way - split process salary from the with open to increase readability
# if you want to handle a specific exception or want to read more data from
# a CSV file you can further break down this function to follow a single
# responsibility principle
def process_salary(csv_reader):
    """Process salary of user from csv file."""
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} salary: {row["salary"]}')
        line_count += 1
    print(f'Completed {line_count} lines.')


with open('employee.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    process_salary(csv_reader)

# wherever you are concerned about performance use ''.join() instead of inplace
# string concatenation, the join method guarantees leaner time concatenation
# accross various python implementations
# Python allocates memory for joined string only one time but when you concatenate
# strings, Python has to allocate new memory for each concatenation because
# Python strings are immutable

# bad way
full_name = first_name + ' ' + last_name
# good way
full_name = ' '.join([first_name, last_name])

# consider using 'is' and 'is not'
# always use 'is' or 'is not' for comparisons with None

if val: # will work when val is not None

# if val is empty dict for example
if val: # will be False in Python
# make as expilict as possible
if val not None: # makes sure only None value will be false

# always use 'is not' instead of 'not..is' to make it more readable
# bad way
if not val is None:
# good way
if val is not None:

# use a function instead of a lambda when binding to and identifier
# the def function object is more useful for string representation and traceback
# then the generic <lambda>
# consider using lambdas in larger expressions so you don't impact the readability
# of the code

# bad way
square = lambda x: x * x
# good way
def square(val):
    return val * val

# make sure to have a return expression in all the places your function exist

# when you need to check for a prefix or suffixes use ''.startswith() and
# ''.endswith() and not string slicing
# slicing is good for when you are operating on a big string or
# performing string operations
# when it is as simple as checking for a prefix use ''.startswith() as it makes
# it more readable


data = 'Hello, how are you doing?'
# bad way
if data[:5] == 'Hello':
# good way
if data.startswith('Hello'):

# use instance()method instead of type() for comparison
# isinstance is true for subclasses

user_ages = {'Harry': 30}
# bad way
type(user_ages) == dict
# good way
if isinstance(user_ages, dict):

# there are multiple ways to compare boolean values in Python

# bad way
if x = False
if x == False
if x is False
# good way
if x:

# good python linters Flake8 and Pylint
# read PEP8 official documentation
# reading good python code on github will help

# using docstrings
# a docstring becomes the __doc__ special attribute of that object
# python recommends using triple double quotesfor docstrings

# some tips always use triple double even if just one line
# no space from at the start of the string
# use period '.' to end the statement in the docstring

# good doc string
def call_weather_api(url, location):
    """Get the weather of specific location.
    Calling weather api to check for weather by using weather api and location.
    Make sure you provice city name only, country and county names won't be accepted
    and will throw exception if not found the city name.
    :param url:  URL of the api to get weather.
    :type url: str
    :param location:  Location of the city to get the weather.
    :type location: str
    :return: Give the weather information of given location.
    :rtype: str
    """
    pass

 # tips for multiline docstrings
 # first line is brieg description of the function or class
 # end of the line has a period
 # there is a one-line fap between the brief descrition and the summary in docstrings

 # multiline with typing
 # dont need to write the param info if you are using the type in python code
 def call_weather_api(url: str, location: str) -> str:
    """Get the weather of specific location.
    Calling weather api to check for weather by using weather api and location.
    Make sure you provice city name only, country and county names won't be
    accepted and will throw exception if not found the city name.
    """
    pass


# module level docstrings
# put at the top of the file to describe the use of the module briefly
# these comments should be before the import as well
# module docstring should focus on the goal of the module, including all the
# method/classes in the module

"""This module contains all the network related request.
This module will check for all the exceptions while making the network calls
and raise exceptions for any unknown exception. Make sure that when you use
this module, you handle these exceptions in client code as:
        NetworkError exception for network calls.
        NetworkNotFound exception if network not found.
"""


import urllib3
import json

# class doc string
class Student:
    """Student class information.
    This class handle actions performed by a student.
    This class provides information about student full name, age, roll-number and  other information.
    Usage:
    import student
    student = student.Student()
    student.get_name()
    >>> 678998
    """

    def __init__(self):
        pass

# useful docstring tools - creates rendered versions of the docstrings
# sphinx
# pycco
# read the docs
# epydocs

# use list comprehension instead of for-loop, filter or map
# unless you have a complex computation
# consider using loops if you have multiple if statements or more than 2 loops

# Generators Vs List Comprehension

# the main difference between generators and list comprehension is that list
# comprehension keeps the data in memory while generators do not

# use list comprehension in the following cases
# when you need t iterate over the list multiple times
# when you need to list methods to play with data that is not available in
# the generator
# when you don't have large data to iterate over an you think keeping data in
# memory wont be an issue

# if file is big then use generator
def read_file(file_name):
    """Read the file line by line."""
    with open(file_name) as fread:
        for line in fread:
            yield line


for line in read_file("logfile.txt"):
    print(line.startswith(">>")

# if file not big can use list comprehension
def read_file(file_name):
    """Read the file line by line."""
    fread = open(file_name, "r")
    data = [line for line in fread if line.startswith(">>")]
    return data


# raising a exception
def division(dividend, divisor):
    """Perform airthmetic division."""
    try:
        return dividend/divisor
    except ZeroDivisionError as zero:
        raise ZeroDivisionError("Please provide greater than 0 value")

# custom exception
class UserNotFoundError(Exception):
    """Raise the exception when user not found."""
    def __init__(self, message=None, erros=None):
        # Calling the base class constructor with the parameter it needs
        super().__init__(message)
        # New for your custom code
        self.errors = errors


def get_user_info(user_obj):
    """Get user information from DB."""
    user = get_user_from_db(user_obj)
    if not user:
        raise UserNotFoundException(f"No user found of this id: {user_obj.id}")

get_user_info(user_obj)

# broader custom exception
class WrongInstanceIDError(Exception):
    """Raise the exception whenever Invalid instance found."""
    def __init__(self, message=None, errros=None):
        # Calling the base class constructor with the parameter it needs
        super().__init__(message)
        # New for your custom code
        self.errors = errors


ec2 = session.get_client('ec2', 'us-east-2')
try:
    parsed = ec2.describe_instances(InstanceIds=['i-badid'])
except ClientError as e:
    logger.error("Received error: %s", e, exc_info=True)
    # Only worry about a specific service error code
    if e.response['Error']['Code'] == 'InvalidInstanceID.NotFound':
        raise WrongInstanceIDError(message=exc_info, errors=e)
