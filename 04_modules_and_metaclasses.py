# Modules
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# modules are simply python files with the .py extension
# the name of the module will be the name of the file
# the idea of a module is to logically separate the functionality of you project
# ------------------------------------------------------------------------------
# user/
# users/payment.py
# users/info.py
# the two modules above separate the user's payment and information functionality
# ------------------------------------------------------------------------------
# modules give you a tool to abstract different layers of your project by placing
# them into different modules

# keep module names short and you can also consider not using an underscore
# or at least keep it minimal
# so dont do:
# import user_card_payment
# import add_product_cart
# Do:
# import payment
# import cart

# try not to use:
# from user import *
# better:
# from user import add_to_cart
# even better and clearer
# import user
# user.add_to_cart()

# __init__ file
# ------------------------------------------------------------------------------
# one of the main uses of __init__.py is to help split modules into
# multiple files
# let's consider the scenario where you hae a module called purchase, which has
# two different classes named as Cart and Payment
# Cart adds the product into the cart
# Payment performs the payment operation for the product

# purchase module


class Cart:
    def add_to_cart(self, cart, product):
        self.execute_query_to_add(cart, product)


class Payment:
    def do_payment(self, user, amount):
        self.exeute_payment_query(user, amount)


# suppose you want to split these two different functionalities into different modules
# to better structure the code
# you can do that by moving the Cart and Payment classes into two different modules,
# as follows:
# purchase/
#     cart.py
#     payment.py

# now you can keep these modules in the __init__.py file to glue it together
# from .cart import Cart
# from .payment import Payment

# if you follow these steps you have given a common interface to the client
# to use different functionality in your package as follows:

# import purchase
#   cart = purchase.Cart()
#   cart.add_to_cart(cart_name, product_name)
#   payment = payment.Payment()
#   payment.do_payment(user, 100)

# this basically allows the user to do a single import
# and still use all the functionality, so the user doesnt have to figure out
# what resides where in you project
# from purchase import Cart, Payment

# this is how you stitch together different submodules into a single module
# you can break large modules into different logical submodules, and
# the user can use only a single module name

# Import modules the correct way
# ------------------------------------------------------------------------------
# inside packages - importing from the same package
# ------------------------------------------------------------------------------
# from foo import bar -> Don't do this
# Do this
# from . import bar -> better way
# the first way means the path is hard coded which you don't want
# as if the name ever changes then you will need to change it everywhere
# the second is relative so is the preferred way
# ------------------------------------------------------------------------------
# outside packages - importing from outside a module
# ------------------------------------------------------------------------------
# from mypackage import * -> BAD
# from mypackage.test import bar -> OK
# import mypackage -> RECOMMENDED WAY
# the second way is ok but when you are importing a lot of packages it gets complicated
# and you dont know which func from where you are using
# whereas the third way is more implicit about what you are using and when
# ------------------------------------------------------------------------------

# Use __ALL__ to prevent imports
# ------------------------------------------------------------------------------
# by using the metaclass __ALL__ you are restricting consumer classes or methods
# to import only specific classes or methods instead of everything from the module

# this only allows what is specified to NOT be imported using '*'
# __all__ = ['class_names', 'function_names']


# Metaclass
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# metaclasses are a blueprint for the creation of a class
# classes create an instance, and metaclasses help to change behaviour
# automatically based on what's needed when it's created
# the main use case of a metaclass is to create and API or library or add
# some complex feature
# whenever you want ot hide a lot of detail and make it easier for the client to use
# your API/library, metaclasses can be really helpful to do that

# good python libraries to that use metaclasses
# flask, Django requests

# Use __new__ for validating subclasses
# ------------------------------------------------------------------------------
# __new__ is called when an instance is being created
# using this method you can easily customize the instance creation
# this method is called before calling __init__ while initializing the instance of
# the class
# let's assume that you need to create all the classes in your module starting
# with awesome. you can use __metaclass__ at the module level to do that
# ------------------------------------------------------------------------------
def awesome_attr(future_class_name, future_class_parents, future_class_attr):
    """
      Return a class object, with the list of its attribute prefix with awesome keyword.
    """
    # pick any attribute that doesn't start with '__' and prefix with awesome
    awesome_prefix = {}
    for name, val in future_class_attr.items():
        if not name.startswith('__'):
            uppercase_attr["_".join("awesome", name)] = val
        else:
            uppercase_attr[name] = val

    # let `type` do the class creation
    return type(future_class_name, future_class_parents, uppercase_attr)


__metaclass__ = uppercase_attr  # this will affect all classes in the module


class Example:
    # global __metaclass__ won't work with "object" though
    # but we can define __metaclass__ here instead to affect only this class
    # and this will work with "object" children
    val = 'yes'
# ------------------------------------------------------------------------------
# link for more info
# https://docs.python.org/3/reference/datamodel.html

# in the below code it uses __new__ metaclass to validate before
# any subclass inherits te abstract or superclass
# ------------------------------------------------------------------------------
from abc import abstractmethod, ABCMeta

class UserAbstract(metaclass=ABCMeta):
    """Abstract base class template, implimenting factory pattern using __new__() initializer."""

    def __new__(cls, *args, **kwargs):
        """Creates an object instance a sets a base property."""
        obj = object.__new__(cls)
        obj.base_property = "Adding Property for each subclass"
        return obj


class User(UserAbstract):
    """Implement UserAbstract class and add its own variable."""

    def __init__(self):
        self.name = "Larry"


user = User()
user.name
# Larry
user.base_property
# Adding Property for each subclass
# ------------------------------------------------------------------------------

# Using __slots__ for faster attribute access
# ------------------------------------------------------------------------------
# __slots__ allows for faster attribute access and memory saving
# dont use until you really need that extra space
# ------------------------------------------------------------------------------

# Change class behaviour using metaclasses
# ------------------------------------------------------------------------------
# instead of creating some complex logic to add a specific behaviour in a class,
# check out the python metaclasses they giv you a nice tool to handle complex
# logic in your code
# __call__
# in the below code __call__ makes sure that the class is not being initiated directly
# from the client code, instead, it uses the static method
# ------------------------------------------------------------------------------
class NoClassInstance:
    """Create the user object."""
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly""")


class User(metaclass=NoClassInstance):

    @staticmethod
    def print_name(name):
        """print name of the provided value."""
        print(f"Name: {name}")


user = User()
# TypeError: Can't instantiate directly
User.print_name("Larry Page")
# Name: Larry Page
# ------------------------------------------------------------------------------

# Descriptors
# ------------------------------------------------------------------------------
# __get__ -> when you access the attribute, this method is automatically being called
# when defined
# __set__ -> when you set the attribute of an instance this methods is calls as:
# obj.attr = 'value'
# __delete__ -> when you want to delete a specific attribute this descriptor is being called

# able to do some extra processing when before user changes anything, making your
# attribute read only.
# it also makes your code cleaner as you dont need to create a specific method to do
# all these complicated validations or check operations




