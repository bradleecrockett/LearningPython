# import is used to make specialty functions available
# These are called modules
import math

'''
This is a multi-line comment
You make it with three single quotes
It helps others read your code
'''

#This is a single line comment in Python

# Hello world is just one line of code
# print() outputs data to the screen
print("Hello World")


# A variable is a place to store values
# Its name is like a label for that value
name = "Brad"
print(name)

# A variable name can contain letters, numbers, or _
# but can't start with a number

# There are 5 data types Numbers, Strings, List, Tuple, Dictionary
# You can store any of them in the same variable

name = 15
print(name)

# there are lots of functionality in the modules
name = math.sin(30)
print(name)

# The arithmetic operators +, -, *, /, %, **, //
# % modulo operator or remainder operator
# ** Exponential calculation
# // Floor Division
print("5 + 2 =", 5 + 2)
print("5 - 2 =", 5 - 2)
print("5 * 2 =", 5 * 2)
print("5 / 2 =", 5 / 2)
print("5 % 2 =", 5 % 2)
print("5 ** 2 =", 5 ** 2)
print("5 // 2 =", 5 // 2)
print("Pi = ", math.pi)

# round can help you... round numbers
# side notefloats should not use == without rounding
print("Pi = ", round(math.pi, 5))

print("Tau= ", math.tau)

# Order of Operation states * and / is performed before + and -

print("1 + 2 - 3 * 2 =", 1 + 2 - 3 * 2)
print("(1 + 2 - 3) * 2 =", (1 + 2 - 3) * 2)

# A string is a string of characters surrounded by " or '
# If you must use a " or ' between the same quote escape it with \
quote = "\"Always remember your unique,"
number = 5

# A multi-line quote
multi_line_quote = ''' just
like everyone else" '''

print(quote + multi_line_quote)


# You can also use concatenation but you need to cast the values as a String (str)
# The result is similar but the accuracy of the float is different
print("I like the quote " + str(number) + multi_line_quote + str(float(number)))

# To keep from printing newlines use end=""
print("I don't like ", end="")
print("newlines")

# You can print a string multiple times with *
print('\n' * 5)
print("Just skipped 5 lines")
