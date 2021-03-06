# ######################################################
#
# https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
#
# ListComprehensions.py
#
# Exercise 7
#
# ######################################################
#
# Let’s say I give you a list saved in a variable:
#
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
#
# Write one line of Python that takes this list a and makes a new list
# that has only the even elements of this list in it.
#
# ######################################################

# Original Problem
a = [-12, 0, 1, 2, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [num for num in a if num % 2 == 0]
print(b)
