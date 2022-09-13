# 1. Introduction
# Python is a popular programming language.
# It was created by Guido van Rossum, and released in 1991.
# -----------------------------PYTHON FEATURES--------------------------------------
#    --*Easy to Code.
#        Python is a very high-level programming language, yet it is effortless to learn.
#      *It easy to read with the by maintaining simple indentation.
#      *It easy to maintain with simple syntax.
#      *Free and Open-Source
#      *Robust Standard Library
#      *It is portable it can run in any os.
#      *python is Interpreted programing language.
#      *python is Object-Oriented .
#      *It is Dynamic programing language.
# -------------------------------It is used for-----------------------------------------
# *web development (server-side),
# *software development,
# *mathematics,
# *system scripting.

#------------------------Python Advantage and Disadvantage:
# Advantage:
#  Easy to Read, Learn and Write
#  Improved Productivity
#  Interpreted Language
#  Dynamically Typed
#  Free and Open-Source
#  Portability
#
# Disadvantage:
# Slow Speed
# Not Memory Efficient
# Weak in Mobile Computing
# Database Access
# Runtime Errors
#------------------------------------------------------------------------------------------------------------------
#2.----------------------------------- Variables---------------------------------
# Variables are containers for storing data values.
# Rules to define the variable Names:
# A variable can have a short name (like x and y) or a more descriptive name
# (age, carname, total_volume). Rules for Python variables:
# * A variable name must start with a letter or the underscore character
# * A variable name cannot start with a number
# * A variable name can only contain alpha-numeric characters and
# underscores (A-z, 0-9, and _ )
# * Variable names are case-sensitive (age, Age and AGE are three different
# variables)

# Example
# variable names:
# myvar = "Bala"
# my_var = "Bala"
# _my_var = "Bala"
# myVar = "Bala"
# MYVAR = "Bala"

# --------------------------Types of variables:-------------------------
# Global Variables:
# Variables that are created outside of a function are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.
# Ex:
# x = "awesome"
# def myfunc():
#     print("Python is " + x)
# myfunc()
#
# Local Variables:
# Variables that are created inside of a function are known as Local variables.
# Ex:
# def myname():
#     x="Bala"
#     print(x+"krishna")
# myname()

# 3. -----------------------------IDE shortcuts----------------------------------
# *.TAB-To get the dropdowm.
# *.CTRL + Q = Exit from IDLE.
# *.ALT + F4 =Close the Active Window.
# *.CTRL + S =Save the Code.
# *.CTRL + F =To look for any word.
# *.CTRL + H =To find and replace.
# *.F5 =Run the Program.
# *.ALT+C = To make the comment.
# *.Ctrl+G =Go to line.
# *.Alt+N=Go to next command.
# *.Alt+U=Uncomment selected code.
# *.Ctrl+Space=Auto-complete entry.


#4.--------------------------------- Operators--------------------------------------
# Python Operators
# Operators are used to perform operations on variables and values.
# In the example below, we use the + operator to add together two values:
# Example:
# print(10 + 5)

# ------------------------------Types of  operators in python---------------------------:
# * Arithmetic operators
# * Assignment operators
# * Comparison operators
# * Logical operators
# * Identity operators
# * Membership operators
# * Bitwise operators

#---------* Arithmetic operators------------------------
# Arithmetic operators are used with numeric values to perform common
# mathematical operations.
# Take the variable valve x=5 y=3
# Operator Name Example
#  *.Addition :It is used to add the two valves.
#  ex:print( x+y)
#  *.Subtraction:It is used to sub the two valves.
#  ex:print( x+y)
#  *.Multiplication :It is used to multiply the two valves.
#  ex:print( x+y)
#  *.Division :It is used to divide the two valves.
#  ex:print( x+y)
#  *.Modulus :It is used to get the reminder  of the two valves.
#  ex:print( x+y)
#  *.Exponentiation :It will used to find the power of the valves.
#  ex:print( x+y)
#  *.Floor division :It will give the int valves as out put.
#  ex:print( x+y)

#------------------------------Python Assignment Operator
#Assignment operators are used to assign values to variables.
# Example:
# Assigning valves x = 5  is same as x = 5
# Increment = x += 3 is same as  x = x + 3
# Decrement= x -= 3 is same as x = x - 3
# Multiply= x *= 3 is same as x = x * 3
# Divide= x /= 3 is same as  x = x / 3
# Modulus= x %= 3 is same as  x = x % 3
# floor= x //= 3 is same as  x = x // 3
# expon= x **= 3 is same as  x = x ** 3
# And= x &= 3  is same as x = x & 3
# Or= x |= 3 is same as x = x | 3
# Power of= x ^= 3 is same as x = x ^ 3
# Greater= x >>= 3 is same as x = x >> 3
# lesser= x <<= 3 is same as x = x << 3

# -----------------------------------Python Comparison Operators:
# Comparison operators are used to compare two values:
# Operator Name Example
#Consider x=3 y=2
# Equal x == y
# Not equal x != y
# Greater than x > y
# Less than x < y
# >= Greater than or equal to
# x >= y<= Less than or
# equal tox <= y

#------------------------------------Logical operators
# Logical operators are used to combine conditional statements.
#
# and	:Returns True if both statements are true
# Ex:
# a = 10
# b = 10
# c = -10
#
# if a > 0 and b > 0:
#     print("The numbers are greater than 0")
#
# if a > 0 and b > 0 and c > 0:
#     print("The numbers are greater than 0")
# else:
#     print("Atleast one number is not greater than 0")
# or	: Returns True if one of the statements is true
# Ex:
# a = 10
# b = -10
# c = 0
#
# if a > 0 or b > 0:
#     print("Either of the number is greater than 0")
# else:
#     print("No number is greater than 0")
#
# if b > 0 or c > 0:
#     print("Either of the number is greater than 0")
# else:
#     print("No number is greater than 0")
# not:Reverse the result, returns False if the result is true
# Ex:
# # Python program to demonstrate
# # logical not operator
#
# a = 10
#
# if not a:
# 	print("Boolean value of a is True")
#
# if not (a%3 == 0 or a%5 == 0):
# 	print("10 is not divisible by either 3 or 5")
# else:
# 	print("10 is divisible by either 3 or 5")

#-----------------------------------------Identity operators
# It will check the adress location of the variables.
# is’ operator – Evaluates to True if the variables on either side
# of the operator point to the same object and false otherwise.
# Ex:
#
# x = 5
# y = 5
# print(x is y)
# id(x)
# id(y)


#----------------------------------------Membership operators
# In membership operators it will check the valve present in the sequence.
# The ‘in’ operator is used to check if a character/ substring/ element exists in a sequence or not.
# Evaluate to True if it finds the specified element in a sequence otherwise False.
# Ex:
# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9]
# for item in list1:
# 	if item in list2:
# 		print("overlapping")
# 	else:
# 		print("not overlapping")


# 5.---------------------------------------Datatypes Introduction:
# Numeric-int,float,complex
# Text-"String"
# Boolen-Bool

#-----------------------------Numeric-----------------------------
# Int:
# Int, or integer is a whole number, positive or negative, without decimals
# of unlimited length.
# Ex:
# x = 1
# y = 35656222554887711
# z = -3255522
#
# print(type(x))
# print(type(y))
# print(type(z))
#
# float:
# Float, or "floating point number" is a
# number, positive or negative, containing one or more decimals.
# Ex:
# x = 1.10
# y = 1.0
# z = -35.59
#
# print(type(x))
# print(type(y))
# print(type(z))
#
# Complex:
# Complex numbers are written with a "j" as the imaginary part:
# Ex:
# x = 3+5j
# y = 5j
# z = -5j
#
# print(type(x))
# print(type(y))
# print(type(z))

#------------------------------------------------Text type
# "String":
# Strings in python are surrounded by either single quotation marks,
# or double quotation marks.
# Ex:
# print("Bala")

#----------------------------------------------BOOLEN----------
# BOOL:In programming you often need to know if an expression is True or False.
# You can evaluate any expression in Python, and get one of two answers, True or False.
# EX:
# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")

# 6.--------------------------------------KEYWORDS--------------------------------
#  Keywor          Description
# =============   ==================
#   and	--->   A logical operator
#   as	--->  To create an alias
#  assert	--->  For debugging
#  break	--->  To break out of a loop
#  class	--->  To define a class
#  continue ---> To continue to the next iteration of a loop
#   def	 ---> To define a function
#   del	---> To delete an object
#  elif	---> Used in conditional statements, same as else if
#  else	---> Used in conditional statements
#  except	---> Used with exceptions, what to do when an exception occurs
# False	---> Boolean value, result of comparison operations
# finally	---> Used with exceptions, a block of code that will be executed no matter
#              if there is an exception or not
# for    --->  To create a for loop
# from   --->  To import specific parts of a module
# global --->  To declare a global variable
# if	---> To make a conditional statement
# import	---> To import a module
# in      ---> To check if a value is present in a list, tuple, etc.
# is	---> To test if two variables are equal
# lambda	---> To create an anonymous function
# None	---> Represents a null value
# nonlocal---> To declare a non-local variable
# not	---> A logical operator
# or	---> A logical operator
# pass	---> A null statement, a statement that will do nothing
# raise	---> To raise an exception
# return	---> To exit a function and return a value
# True    ---> Boolean value, result of comparison operations
# try	---> To make a try...except statement
# while	---> To create a while loop
# with	---> Used to simplify exception handling
# yield   ---> To end a function, returns a generator