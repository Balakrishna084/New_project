# DATA_Structure:
# Organizing, managing and storing data is important as it enables easier access and efficient modifications.
# Data Structures allows you to organize your data in such a way that enables you to store collections of data,
# relate them and perform operations on them accordingly.
# There are four major data Structure in python:
# *List
# *Tuple
# *Dictionaries
# *set
# ---------------------------------------------------------------List
# 1.list:
# Lists are used to store multiple items in a single variable.Lists are very similar to arrays. They can contain
# any type of variable, and they can contain as many variables as you wish. Lists can also be iterated over in a
# very simple manner. Here is an example of how to build a list.
# *List items are ordered, changeable, and allow duplicate values.
#
# List Items
# List items are ordered, changeable, and allow duplicate values.
# Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
# Allow Duplicates
# Since lists are indexed, lists can have items with the same value
Ex:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# List Length:
# To determine how many items a list has, use the len() function:
# Example:
thislist1= ["apple", "banana", "cherry"]
print(len(thislist))


# List Items - Data Types:
# List items can be of any data type:
# Example:
list0 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
print(list0,list2,list3,list4 )

# The list() Constructor:
# It is also possible to use the list() constructor when creating a new list.
# Example
# Using the list() constructor to make a List:
thislist5 = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist5)

# Python - Access List Items
# Access Items
# List items are indexed and you can access them by referring to the index number:
# Example
# Print the second item of the list:
thislist6 = ["apple", "banana", "cherry","kiwi"]
print(thislist6[1])
print(thislist6[2])
print(thislist6[3])
print(thislist6[-2])
print(thislist6[0:2])
print(thislist6[-1:-3])
#This example returns the items from the beginning to, but NOT including, "kiwi":
thislist_1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


# Check if Item Exists:
# To determine if a specified item is present in a list use the in keyword:
# Check if "apple" is present in the list:
thislist_2 = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# SOME BUILT IN FUNCTIONS OF LIST:
# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index:
# Example:
# Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Add List Items
# Append Items
# To add an item to the end of the list, use the append() method:
# Example:
# Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Extend List:
# To append elements from another list to the current list, use the extend() method.
# Example:
# Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Python - Remove List Items
# Remove Specified Item
# The remove() method removes the specified item.
# Example
# Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index
# The pop() method removes the specified index.
# Example:
# Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# The del keyword also removes the specified index:
# Example
# Remove the first item:
thislist_4 = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist_4)


# The del keyword can also delete the list completely.
# Example
# Delete the entire list:
thislist_9 = ["apple", "banana", "cherry"]
del thislist_9


# Clear the List:
# The clear() method empties the list.
# The list still remains, but it has no content.
# Example
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Loop Through a List
# You can loop through the list items by using a for loop:
# Example
# Print all items in the list, one by one:
 thislist_32 = ["apple", "banana", "cherry"]
 for x in thislist_32:
   print(x)

# List Methods
# Python has a set of built-in methods that you can use on lists.

# Method	Description
# append()==	Adds an element at the end of the list
# clear() ==	Removes all the elements from the list
# copy() ==	Returns a copy of the list
# count()	== Returns the number of elements with the specified value
# extend() ==	Add the elements of a list (or any iterable), to the end of the current list
# index() ==	Returns the index of the first element with the specified value
# insert() ==	Adds an element at the specified position
# pop() ==	Removes the element at the specified position
# remove() ==	Removes the item with the specified value
# reverse() ==	Reverses the order of the list
# sort() ==	Sorts the list


# -----------------------------------------------Tuple
# Tuple:Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

Example:
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:

# Access Tuple Items
# You can access tuple items by referring to the index number, inside square brackets:
# Example
# Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
# Example:
# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Remove Items:
# Tuples are unchangeable, so you cannot remove items from it,
# but you can use the same workaround as we used for changing and adding tuple items:
thistuple_= ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)


Unpacking a Tuple:
When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
Example:
Packing a tuple:
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Python - Loop Tuples
# Loop Through a Tuple
# You can loop through the tuple items by using a for loop.
#
# Example
# Iterate through the items and print the values:

thistuple_22 = ("apple", "banana", "cherry")
for x in thistuple_22:
  print(x)

# Tuple Methods :
# Python has two built-in methods that you can use on tuples.
#
# Method	Description
# count()	==Returns the number of times a specified value occurs in a tuple
# index()	==Searches the tuple for a specified value and returns the position of where it was found

# -------------------------------------------------------Dictionaries
# Dictionary:
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Dictionaries are written with curly brackets, and have keys and values:

Example:
Create and print a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


#Dictionary items are ordered, changeable, and does not allow duplicates.
# Ordered or Unordered:
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
# Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.
# Changeable:
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
# Duplicates Not Allowed:
# Dictionaries cannot have two items with the same key:

# Accessing Items:
# You can access the items of a dictionary by referring to its key name, inside square brackets:
# Example
# Get the value of the "model" key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

# Get Values
# # The values() method will return a list of all the values in the dictionary.
# Example
# Get a list of the values:

x = thisdict.values()


# Make a change in the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change


# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:
# Example
# Check if "model" is present in the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


# Change Values:
# You can change the value of a specific item by referring to its key name:
# Example
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
# Example
# Update the "year" of the car by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})


# Adding Items:
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

Example:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# Update Dictionary
# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
# The argument must be a dictionary, or an iterable object with key:value pairs.
# Example
# Add a color item to the dictionary by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})


# Removing Items
# There are several methods to remove items from a dictionary:

Example
# The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#The del keyword can also delete the dictionary completely:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.

#The clear() method empties the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

Print all values in the dictionary, one by one:

for x in thisdict:
  print(thisdict[x])
for x in thisdict.values():
  print(x)
for x in thisdict.keys():
  print(x)


# Method	Description
# clear() ==	Removes all the elements from the dictionary
# copy() ==	Returns a copy of the dictionary
# fromkeys() ==	Returns a dictionary with the specified keys and value
# get()	== Returns the value of the specified key
# items()==	Returns a list containing a tuple for each key value pair
# keys() ==	Returns a list containing the dictionary's keys
# pop()	== Removes the element with the specified key
# popitem() ==	Removes the last inserted key-value pair
# setdefault() ==	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update() ==	Updates the dictionary with the specified key-value pairs
# values() ==	Returns a list of all the values in the dictionary


#---------------------------------------------------------SET
    