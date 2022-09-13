# 1.Decision Making,:
# Decision making is anticipation of conditions occurring while execution of the program and
# specifying actions taken according to the conditions.
# Decision structures evaluate multiple expressions which produce TRUE or FALSE as outcome.,
# Python has the following decision-making statements:
# *if statements
# *if-else statements
# *if-elif ladder
# *Nested statements
# --------------------------------------------if statement
# *if statement:
# if statement is the most simple form of decision-making statement. It takes an expression and
# checks if the expression evaluates to True
# then the block of code in if statement will be executed.
# syntax:
# if ( expression ):
#   Statement 1
#   Statement 2
#   .
#   Statement n
#
# Ex:
# num = 5
# if ( num >= 10):
#   print(“num is greater than 10”)
# print(“if block ended”)
# -----------------------------------------------------if-else statements
# *if-else statements:
#   From the name itself, we get the clue that the if-else statement checks the expression and executes
#   the if block when the expression is True otherwise it will execute the else block of code.
#   The else block should be right after
#   if block and it is executed when the expression is False.
# syntax:
# if( expression ):
#   Statement
# else:
#   Statement
# EX:
# number1 = 20 ; number2 = 30
# if(number1 >= number2 ):
#   print(“number 1 is greater than number 2”)
# else:
#   print(“number 2 is greater than number 1”)
# -----------------------------------------if-elif ladder
# if-elif ladder
# In Python, we have an elif keyword to chain multiple conditions one after another. With elif ladder,
# we can make complex decision-making statements.
#The elif statement helps you to check multiple expressions and it executes the code as soon as
# one of the conditions evaluates to True.
# Syntax:
# if( expression1 ):
#   statement
# elif (expression2 ) :
#   statement
# elif(expression3 ):
#   statement
# .
# .
# else:
#   statement
#Ex:
# print(“Select your ride:”)
# print(“1. Bike”)
# print(“2. Car”)
# print(“3. SUV”)
#
# choice = int( input() )
#
# if( choice == 1 ):
#   print( “You have selected Bike” )
# elif( choice == 2 ):
#   print( “You have selected Car” )
# elif( choice == 3 ):
#   print( “You have selected SUV” )
# else:
#   print(“Wrong choice!“)
-----------------------------------------------------------------------Nested statements
# Nested statement
# In very simple words, Nested if statements is an if statement inside another if statement. Python allows us
# to stack any number of if statements inside the block of another
# if statements. They are useful when we need to make a series of decisions.
# Syntax:
# if (expression):
#   if(expression):
#     Statement of nested if
#   else:
#     Statement of nested if else
# else:
#   statement
# Ex:num1 = int( input())
# num2 = int( input())
#
# if( num1>= num2):
#     if(num1 == num2):
#         print(f'{num1} and {num2} are equal')
#     else:
#         print(f'{num1} is greater than {num2}')
# else:
#     print(f'{num1} is smaller than {num2}')


------------------------------------------------2.loops--------------------------------------------------------------
# Loops:Loops are one of the most powerful and basic concepts in programming. A loop can contain a set of
# statements that keeps on executing until a specific condition is reached.
#
# Types of loop:
# *for
# *while
# +---------------------------------------------for loop----------------------------------
# *for loop:For loop in Python is used to iterate over a sequence of items like list, tuple, set, dictionary,
# string
# or any other iterable objects.
# syntax:
# for item in sequence:
#     body of for loop
#
# Ex:
# for item in [1,2,3,4]:
#     print( item)

# Using else in for loop
# In Python programming, the loops can also have an
# else part which will be executed once when the loop terminates.
# Ex:
# for i in [1, 2, 3, 4]:
#   print(i)
# else:
#   print(“The loop ended”)
--------------------------------------------while loop-------------------------------------
# While loop:
# The while loop in Python executes a block of code until the specified condition becomes False.
# syntax:
# while( condition):
#   Body of while
#   Inside while block
#
# Ex:count = 0
# while( count< 10):
#   print(count)
#   count = count + 2

# ------------------------------------------------------------Loop Control Statements in Python
# 3.Loop Control Statements in Python
# *Break
# *Continue
# *pass
# ----------------------------------------Break statement
# The break statement inside a loop is used to exit out of the loop. Sometimes in a program,
# we need to exit the loop when a certain condition is fulfilled.
# Ex:
# num = 0
# while( num <10 ):
#     num +=1
#     if(num==5): break
#     print( num )
#
# print("Loop ended")
# -------------------------------------------continue statement
# Continue statement:The continue statement is used to skip the next statements in the loop.
# When the program reaches the continue statement, the program skips the statements after
# continue and the flow reaches the next iteration of the loop.
# Ex:
# num = 0
# while( num <10 ):
#     num +=1
#     if(num==5): continue
#     print( num )
#
# print("Loop ended")
# --------------------------------------------pass statement
# The pass is a null statement and the Python interpreter returns a no-operation (NOP) after reading the pass statement.
# Nothing happens when the pass statement is executed. It is used as a placeholder when implementing new methods or we
# can use them in exception handling.
# Ex:
# nums = [1,2,3,4]
# for num in nums:
#   pass
#
# print(nums)