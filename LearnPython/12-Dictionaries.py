# Python Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


# Dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*,
#  changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered.
# In Python 3.6 and earlier, dictionaries are unordered.
# Dictionaries are written with curly brackets, and have keys and values:


# Create and print a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)



# Dictionary Items
# Dictionary items are ordered, changeable, and does not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
# Print the "brand" value of the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])



# Ordered or Unordered?
# As of Python version 3.7, dictionaries are ordered.
# In Python 3.6 and earlier, dictionaries are unordered.
# When we say that dictionaries are ordered,
# it means that the items have a defined order, and that order will not change.
# Unordered means that the items does not have a defined order,
# you cannot refer to an item by using an index.


# Changeable
# Dictionaries are changeable,
# meaning that we can change, add or remove items after the dictionary has been created.

# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key:

# Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)



# Python - Access Dictionary Items
# Accessing Items
# You can access the items of a dictionary by 
# referring to its key name, inside square brackets:

# Get the value of the "model" key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]


# There is also a method called get() that will give you the same result:
# Get the value of the "model" key:

x = thisdict.get("model")


# Get Keys
# The keys() method will return a list of all the keys in the dictionary.

# Get a list of the keys:

x = thisdict.keys()

# The list of the keys is a view of the dictionary,
# meaning that any changes done to the dictionary will be reflected in the keys list.


# Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change




# Python - Change Dictionary Items
# Change Values
# You can change the value of a specific item by referring to its key name:


# Change the "year" to 2018:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018


# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.


# Update the "year" of the car by using the update() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})



# Python - Add Dictionary Items
# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)



# Update Dictionary
# The update() method will update the dictionary 
# with the items from a given argument. If the item does not exist, the item will be added.
# The argument must be a dictionary, or an iterable object with key:value pairs.


# Add a color item to the dictionary by using the update() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})




# Python - Remove Dictionary Items
# Removing Items
# There are several methods to remove items from a dictionary:
# The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


# The popitem() method removes the last inserted 
# item (in versions before 3.7, a random item is removed instead):

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)




# The del keyword removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)




# The del keyword can also delete the dictionary completely:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.




# The clear() method empties the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)



# Python - Loop Dictionaries
# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.

# When looping through a dictionary,
# the return value are the keys of the dictionary,
# but there are methods to return the values as well.


# Print all key names in the dictionary, one by one:

for x in thisdict:
  print(x)

# Print all values in the dictionary, one by one:

for x in thisdict:
  print(thisdict[x])



# You can also use the values() method to return values of a dictionary:

for x in thisdict.values():
  print(x)



# You can use the keys() method to return the keys of a dictionary:

for x in thisdict.keys():
  print(x)



# Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
  print(x, y)


# Python - Copy Dictionaries
# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1,
# because: dict2 will only be a reference to dict1,
# and changes made in dict1 will automatically also be made in dict2.

# There are ways to make a copy, one way is to use the built-in Dictionary method copy().


# Make a copy of a dictionary with the copy() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)



# Another way to make a copy is to use the built-in function dict().

# Make a copy of a dictionary with the dict() function:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)




# Python - Nested Dictionaries
# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.


# Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}


# Or, if you want to add three dictionaries into a new dictionary:


# Create three dictionaries,
# then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}



# Access Items in Nested Dictionaries
# To access items from a nested dictionary,
#  you use the name of the dictionaries, starting with the outer dictionary:


# Print the name of child 2:

print(myfamily["child2"]["name"])




# Python Dictionary Methods
# Dictionary Methods
# Python has a set of built-in methods that you can use on dictionaries.

#   Method	        Description
#   clear()	        Removes all the elements from the dictionary
#   copy()	        Returns a copy of the dictionary
#   fromkeys()	    Returns a dictionary with the specified keys and value
#   get()	          Returns the value of the specified key
#   items()	        Returns a list containing a tuple for each key value pair
#   keys()	        Returns a list containing the dictionary's keys
#   pop()	          Removes the element with the specified key
#   popitem()	      Removes the last inserted key-value pair
#   setdefault()	  Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#   update()	      Updates the dictionary with the specified key-value pairs
#   values()	      Returns a list of all the values in the dictionary