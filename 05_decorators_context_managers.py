# Decorators
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# decorators help you add behaviour to functions or objects dynamically
# without changing the function or object behaviour
# imagine you have several functions in your code and you need to add logging
# in all of them so that when they get executed the function name gets logged
# in the log file or prints to the console
# adding a line to each function would take long and be quite error prone
# the better way would be to add a decorator on top of each function/class
# this is much more effective and doesn't have the risk of adding new bugs
# to existing code

# decorators can be applied to functions and they have the ability to run
# before and after the function they wrap
# decorators help run additional code in functions, this allows you to access
# and modify input args and return values
# helping in multiple places
# Rate Limiting, Caching Values, Timing the runtime of a function, Logging purposes
# Caching exceptions or raising them, Authentication

# API frameworks like flask heavily rely on decorators to turn functions into API's
# the below code turns the function hello into an API using the route decorator
# ------------------------------------------------------------------------------
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


# in the below example to_upper() is a decorator which takes a functions as
# a parameter and converts string to uppercase
# say() uses to_upper() as a decorator when python executes the function say()
# python passes say() to to_upper() at execution time and returns a function object
# which gets executed when called as say()
# ------------------------------------------------------------------------------
def to_upper_case(func):
    def wrapper():
        text = func()
        if not isinstance(text, str):
            raise TypeError("Not a string type")
        return text.upper()

    return wrapper


@to_upper_case
def say():
    return "welcome"


@to_upper_case
def hello():
    return "hello"


say()  # WELCOME
hello()  # HELLO


# ------------------------------------------------------------------------------
# a good example would be if you want users to login before seeing any content
# on your website
# you could use a login decorator on any function which allow users to access your
# website which would force the user to login

# multiple decorators
# ------------------------------------------------------------------------------
# they get applied from bottom to top
# so the top gets called first and the bottom last
# ------------------------------------------------------------------------------


def add_prefix(func):
    def wrapper():
        text = func()
        result = " ".join([text, "Larry Page!"])
        return result

    return wrapper


def to_upper_case(func):
    def wrapper():
        text = func()
        if not isinstance(text, str):
            raise TypeError("Not a string type")
        return text.upper()

    return wrapper


@to_upper_case
@add_prefix
def say():
    return "welcome"


say()  # WELCOME LARRY PAGE!


# ------------------------------------------------------------------------------


# decorator with multiple arguments
# ------------------------------------------------------------------------------
def to_upper_case(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        if not isinstance(text, str):
            raise TypeError("Not a string type")
        return text.upper()

    return wrapper


@to_upper_case
def say(greet):
    return greet


say("hello, how you doing")  # 'HELLO, HOW YOU DOING'
# ------------------------------------------------------------------------------

# when using decorators you will always lose information such as __name__, __doc__
# as it will display the information of the wrapper function inside the decorator
# to overcome this we need to you functools.wrap
# it takes a function used in a decorator and adds the functionality
# of copying over the function name, docstring, arguments list, and so on
# can also use decorator
# from decorator import decorator
# ------------------------------------------------------------------------------
from functools import wraps


def logging(func):
    @wraps(func)
    def logs(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return logs


@logging
def foo(x):
    """does some math"""
    return x + x * x


print(foo.__name__)  # prints 'f'
print(foo.__doc__)  # prints 'does some math'
# ------------------------------------------------------------------------------

# Class decorators
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# to make any class callable we need the __call__()
# this allows a class instance to be called as a function
# __call__ makes it possible to create classes as decorators and return the
# class object to use as a function

# Context Managers
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
with open('temp.txt') as fh:
    for line in fh:
        print(f'{line}')


# ------------------------------------------------------------------------------
# in the above code we are using a context manager by using 'with'
# a context manager helps you better handle resources

# Build context manager
# ------------------------------------------------------------------------------
# to create a with statement all you need to do is add the __enter__ and __exit__
# python will call these two methods when it needs to manage resources
# ------------------------------------------------------------------------------
class ReadFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


file_name = "test.txt"

with ReadFile(file_name) as fread:
    fread.write("Learning context manager")
    fread.write("Writing into file")
# ------------------------------------------------------------------------------

# __enter__ -> return an object that is assigned to the variable after as in a
# context manager block, this object usually is self
# __exit__ -> calls the original context manager, not the one that is returned by __enter__
# __exit__ -> wont be called if there is an exception or error in the __init__ or __enter__

# instead of writing classes to create a context manager, python provides a library
# called contextlib.contextmanager decorator
# it is more convenient to write the context manager instead of writing classes
# you dont need to write the whole class with __enter__ and __exit__

# the contextlib.contextmanager decorator is a generator-based factory function for
# a resource that will automaticlly support the with statement
# ------------------------------------------------------------------------------

from contextlib import contextmanager


@contextmanager
def write_file(file_name):
    try:
        fread = open(file_name, "w")
        yield fread
    finally:
        fread.close()


with read_file("accounts.txt") as f:
    f.write("Hello, how you are doing")
    f.write("Writing into file")
# ------------------------------------------------------------------------------

# some examples
# ------------------------------------------------------------------------------
# https://docs.python.org/2/library/sqlite3.html -> python 2?
# using-the-connection-as-a-context-manager
# in the below code we are using a context manager that automatically
# commits and rolls back in case of failure
# ------------------------------------------------------------------------------
import sqlite3

con = sqlite3.connect(":memory:")
con.execute("create table person (id integer primary key, firstname varchar unique)")

# Successful, con.commit() is called automatically afterwards
with con:
    con.execute("insert into person(firstname) values (?)", ("Joe",))

# con.rollback() is called after the with block finishes with an exception, the
# exception is still raised and must be caught
try:
    with con:
        con.execute("insert into person(firstname) values (?)", ("Joe",))
except sqlite3.IntegrityError:
    print("couldn't add Joe twice")
# ------------------------------------------------------------------------------
# writing test
# while writing test, a lot of time you want to mock specific services of tests
# with different kind of exceptions thrown by code
# in these cases a context manager is really useful
# testing libraries like pytest have features that allow you to use a context
# manager to write the code that tests those exception or mock services
# ------------------------------------------------------------------------------
import pytest


def divide_numbers(first, second):
    if isinstance(first, int) and isinstance(second, int):
        raise ValueError("Value should be int")

    try:
        return first/second
    except ZeroDivisionError:
        print("Value should not be zero")
        raise


def test_divide_numbers():
    with pytest.raises(ValueError):
        divide_numbers("1", 2)
# ------------------------------------------------------------------------------
# and for mocking
# ------------------------------------------------------------------------------
# with mock.patch('new_class.method_name'):
#     call_function()

# shared resource
# ------------------------------------------------------------------------------
from filelock import FileLock

def write_file(file_name):
    with FileLock(file_name):
        # work with the file as it is now locked
        print("Lock acquired.")
# ------------------------------------------------------------------------------

# remote connection - one of the best places to use context manager
# ------------------------------------------------------------------------------
class Protocol:
    def __init__(self, host, port):
        self.host, self.port = host, port

    def __enter__(self):
        self._client = socket()
        self._client.connect((self.host, self.port))
        return self

    def __exit__(self, exception, value, traceback):
        self._client.close()

    def send(self, payload):
        <code for sending data>

    def receive(self):
        <code for receiving data>


with Protocol(host, port) as protocol:
     protocol.send(['get', signal])
     result = protocol.receive()
# ------------------------------------------------------------------------------
