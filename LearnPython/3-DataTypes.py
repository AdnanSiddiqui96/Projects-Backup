# Python Data Types
# Built-in Data Types
# In programming, data type is an important concept.

# Variables can store data of different types, and different types can do different things.

# Python has the following data types built-in by default, in these categories:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType



# Getting the Data Type
# You can get the data type of any object by using the type() function:
# Print the data type of the variable x:

x = 5
print(type(x))


# Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:

# Data Type	
# x = "Hello World"	str	
# x = 20	int	
# x = 20.5	float	
# x = 1j	complex	
# x = ["apple", "banana", "cherry"]	list	
# x = ("apple", "banana", "cherry")	tuple	
# x = range(6)	range	
# x = {"name" : "John", "age" : 36}	dict	
# x = {"apple", "banana", "cherry"}	set	
# x = frozenset({"apple", "banana", "cherry"})	frozenset	
# x = True	bool	
# x = b"Hello"	bytes	
# x = bytearray(5)	bytearray	
# x = memoryview(bytes(5))	memoryview	
# x = None	NoneType



# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:


# x = str("Hello World")	str	
# x = int(20)	int	
# x = float(20.5)	float	
# x = complex(1j)	complex	
# x = list(("apple", "banana", "cherry"))	list	
# x = tuple(("apple", "banana", "cherry"))	tuple	
# x = range(6)	range	
# x = dict(name="John", age=36)	dict	
# x = set(("apple", "banana", "cherry"))	set	
# x = frozenset(("apple", "banana", "cherry"))	frozenset	
# x = bool(5)	bool	
# x = bytes(5)	bytes	
# x = bytearray(5)	bytearray	
# x = memoryview(bytes(5))	memoryview




# Python Numbers
# There are three numeric types in Python:

int
float
complex
# Variables of numeric types are created when you assign a value to them:
x = 1    # int
y = 2.8  # float
z = 1j   # complex
# To verify the type of any object in Python, use the type() function:


print(type(x))
print(type(y))
print(type(z))
# Int
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.


# Integers:

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))



# Float
# Float, or "floating point number" is a number, positive or negative,
# containing one or more decimals.


# Floats:

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
# Float can also be scientific numbers with an "e" to indicate the power of 10.

# Floats:

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))


# Complex
# Complex numbers are written with a "j" as the imaginary part:


# Complex:

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))



# Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods:
# Convert from one type to another:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
# Note: You cannot convert complex numbers into another number type.

# Random Number
# Python does not have a random() function to make a random number,
#  but Python has a built-in module called random that can be used to make random numbers:


# Import the random module, and display a random number between 1 and 9:

import random

print(random.randrange(1, 10))



# Python Casting
# Specify a Variable Type
# There may be times when you want to specify a type on to a variable.
# This can be done with casting. Python is an object-orientated language,
#  and as such it uses classes to define data types, including its primitive types.
# Casting in python is therefore done using constructor functions:
# int() - constructs an integer number from an integer literal,
# a float literal (by removing all decimals),
# or a string literal (providing the string represents a whole number)
# float() - constructs a float number from an integer literal,
# a float literal or a string literal (providing the string represents a float or an integer)
# str() - constructs a string from a wide variety of data types,
#  including strings, integer literals and float literals

# Integers:
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3



# Floats:
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2


# Strings:
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'




# Python Strings
# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
# You can display a string literal with the print() function:

print("Hello")
print('Hello')


# Assign String to a Variable
# Assigning a string to a variable is done with the variable name followed by an
#  equal sign and the string:
a = "Hello"
print(a)


# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:
# You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
# Or three single quotes:


a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
# Note: in the result, the line breaks are inserted at the same position as in the code.



# Strings are Arrays
# Like many other popular programming languages,
#  strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type,
# a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.


# Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])
# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.
# Loop through the letters in the word "banana":

for x in "banana":
  print(x)
# Learn more about For Loops in our Python For Loops chapter.
# String Length
# To get the length of a string, use the len() function.
# The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))



# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.


# Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)
# Use it in an if statement:
# Print only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
# Learn more about If statements in our Python If...Else chapter.

# Check if NOT
# To check if a certain phrase or character is NOT present in a string,
# we can use the keyword not in.


# Check if "expensive" is NOT present in the following text:

txt = "The best things in life are free!"
print("expensive" not in txt)
# Use it in an if statement:


# print only if "expensive" is NOT present:

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")



# Python - Slicing Strings
# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
# Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])
# Note: The first character has index 0.

# Slice From the Start
# By leaving out the start index, the range will start at the first character:


# Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])


# Slice To the End
# By leaving out the end index, the range will go to the end:


# Get the characters from position 2, and all the way to the end:
# b = "Hello, World!"
# print(b[2:])


# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
# Get the characters:

# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):

b = "Hello, World!"
print(b[-5:-2])




# Python - Modify Strings
# Python has a set of built-in methods that you can use on strings.
# Upper Case
# ExampleGet your own Python Server
# The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())


# Lower Case
# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())


# Remove Whitespace
# Whitespace is the space before and/or after the actual text,
# and very often you want to remove this space.
# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


# Replace String
# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))



# Split String
# The split() method returns a list where the text between the 
# specified separator becomes the list items.
# The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']




# Python - String Concatenation
# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.
# Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)



# To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)



# Python - Format - Strings
# String Format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:



# age = 36
# txt = "My name is John, I am " + age
# print(txt)
# But we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them,
# and places them in the string where the placeholders {} are:
# Use the format() method to insert numbers into strings:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


# The format() method takes unlimited number of arguments,
# and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


# Python - Escape Characters
# Escape Character
# To insert characters that are illegal in a string, use an escape character.

# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that
# is surrounded by double quotes:
# You will get an error if you use double quotes inside a string that is surrounded by double quotes:

# txt = "We are the so-called "Vikings" from the north."
# To fix this problem, use the escape character \":

# The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."
# Escape Characters
# Other escape characters used in Python:

# Code	    Result	
# \'	    Single Quote	
# \\	    Backslash	
# \n	    New Line	
# \r	    Carriage Return	
# \t	    Tab	
# \b	    Backspace	
# \f	    Form Feed	
# \ooo	    Octal value	
# \xhh	    Hex value



# Python - String Methods
# String Methods
# Python has a set of built-in methods that you can use on strings.

# Note: All string methods return new values. They do not change the original string.

# Method	        Description
# capitalize()	    Converts the first character to upper case
# casefold()	    Converts string into lower case
# center()	        Returns a centered string
# count()	        Returns the number of times a specified value occurs in a string
# encode()	        Returns an encoded version of the string
# endswith()	    Returns true if the string ends with the specified value
# expandtabs()	    Sets the tab size of the string
# find()	        Searches the string for a specified value and returns the position of where it was found
# format()	        Formats specified values in a string
# format_map()	    Formats specified values in a string
# index()	        Searches the string for a specified value and returns the position of where it was found
# isalnum()	        Returns True if all characters in the string are alphanumeric
# isalpha()	        Returns True if all characters in the string are in the alphabet
# isdecimal()	    Returns True if all characters in the string are decimals
# isdigit()	        Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	        Returns True if all characters in the string are lower case
# isnumeric()	    Returns True if all characters in the string are numeric
# isprintable()	    Returns True if all characters in the string are printable
# isspace()	        Returns True if all characters in the string are whitespaces
# istitle()	        Returns True if the string follows the rules of a title
# isupper()	        Returns True if all characters in the string are upper case
# join()	        Joins the elements of an iterable to the end of the string
# ljust()	        Returns a left justified version of the string
# lower()	        Converts a string into lower case
# lstrip()	        Returns a left trim version of the string
# maketrans()	    Returns a translation table to be used in translations
# partition()	    Returns a tuple where the string is parted into three parts
# replace()	        Returns a string where a specified value is replaced with a specified value
# rfind()	        Searches the string for a specified value and returns the last position of where it was found
# rindex()	        Searches the string for a specified value and returns the last position of where it was found
# rjust()	        Returns a right justified version of the string
# rpartition()	    Returns a tuple where the string is parted into three parts
# rsplit()	        Splits the string at the specified separator, and returns a list
# rstrip()	        Returns a right trim version of the string
# split()	        Splits the string at the specified separator, and returns a list
# splitlines()	    Splits the string at line breaks and returns a list
# startswith()	    Returns true if the string starts with the specified value
# strip()	        Returns a trimmed version of the string
# swapcase()	    Swaps cases, lower case becomes upper case and vice versa
# title()	        Converts the first character of each word to upper case
# translate()	    Returns a translated string
# upper()	        Converts a string into upper case
# zfill()	        Fills the string with a specified number of 0 values at the beginning



# Python Booleans
# Booleans represent one of two values: True or False.
# Boolean Values
# In programming you often need to know if an expression is True or False.
# You can evaluate any expression in Python, and get one of two answers, True or False.
# When you compare two values, the expression is evaluated and Python returns the Boolean answer:


print(10 > 9)
print(10 == 9)
print(10 < 9)


# When you run a condition in an if statement, Python returns True or False:
# Print a message based on whether the condition is True or False:

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return,
# Evaluate a string and a number:
print(bool("Hello"))
print(bool(15))


# Evaluate two variables:

x = "Hello"
y = 15

print(bool(x))
print(bool(y))


# Most Values are True
# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.
# The following will return True:

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


# Some Values are False
# In fact, there are not many values that evaluate to False,
# except empty values, such as (), [], {}, "", the number 0,
# and the value None. And of course the value False evaluates to False.


# The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


# One more value, or object in this case, evaluates to False,
# and that is if you have an object that is made from a class
# with a __len__ function that returns 0 or False:


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


# Functions can Return a Boolean
# You can create functions that returns a Boolean Value:
# Print the answer of a function:

def myFunction() :
  return True

print(myFunction())


# You can execute code based on the Boolean answer of a function:
# Print "YES!" if the function returns True, otherwise print "NO!":

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


# Python also has many built-in functions that return a boolean value,
# like the isinstance() function, which can be used to 
# if an object is of a certain data type:


# Check if an object is an integer or not:

x = 200
print(isinstance(x, int))